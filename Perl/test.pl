#!/usr/bin/perl
print("Hello, Perl\n\n");

# subroutine
sub funcName(value) {
  print("$value")
  #return ($value); # when arguments/parameters are pasing through function/subroutine
}

&funcName("5"); # (specify Arguments in round brackets)
