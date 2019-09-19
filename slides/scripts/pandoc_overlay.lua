--[[
    This filter simplifies the creation of beamer slides from markdown. See
    README.md for documentation.
]]


function latex(text)
    return pandoc.RawInline("latex", text)
end


function findOverlaySpec(block)
    -- This will check to see if the block starts with an overlay
    -- specification followed by a space. If so, it inserts the appropriate
    -- LaTeX code with that specification around the block.
    if FORMAT == 'beamer' and #block.content > 2 then
        local firstInline = block.content[1]
        if firstInline.tag == 'Str' and block.content[2].tag == 'Space' then
            local first, last = string.find(firstInline.text, '^[*+]?<[^\\s]+>$')
            if first then
                table.remove(block.content, 1)
                if FORMAT == 'beamer' then
                    local overlaySpec = string.sub(firstInline.text, first, last)
                    local inline = latex('\\onslide' .. overlaySpec .. '{')
                    table.insert(block.content, 1, inline)
                    table.remove(block.content, 2)  -- Remove <Space>
                    table.insert(block.content, latex('}'))
                end
            end
        end
    end
    return block
end


function handlePlain(plain)
    return findOverlaySpec(plain)
end


function handlePara(para)
    return findOverlaySpec(para)
end


function handleInline(inline)
    if FORMAT == 'beamer' and inline.attr.attributes.slides then
        table.insert(inline.content, 1, latex('\\onslide' .. inline.attr.attributes.slides .. '{'))
        table.insert(inline.content, latex('}'))
    end
    return inline.content
end


local BEAMER_FILTER = {
    {Span = handleInline},
    {Para = handlePara},
    {Plain = handlePlain}
}


return BEAMER_FILTER
