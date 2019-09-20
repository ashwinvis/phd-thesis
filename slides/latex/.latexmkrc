@default_files = ('slides.tex');

$pdf_mode = 1;
$biber_silent_switch = ('--onlylog -quiet');

$clean_ext = "bbl nav out snm";


ensure_path('TEXINPUTS', '../');
add_cus_dep('md', 'tex', 0, 'md2tex');
sub md2tex {
  return system("make -j -f ../Makefile \"$_[0].tex\"");
}

# vim:set ft=perl
