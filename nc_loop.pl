#!/usr/bin/perl
# author			: @g0vandS, Govand Sinjari
# license           : MIT

$a='';
for $n(1..20) {
for $d(0..9) {
$num = $a . $d;
$num .= ('0'x(20-length($num)));
print "$num\n";
$g = `echo $num|nc hackyeaster.hacking-lab.com 1234`;
print "$g\n";
($out) = $g=~/(\d+)[<>]/;
if($out>=$n) {
$a.=$d;
last;
}
print "output: '$out'\n";
}
}