#!/usr/bin/env ruby

pattern = /School/

if ARGV.length != 1
  puts "Usage: ./0-simply_match_school.rb <string>"
  exit(1)
end

string = ARGV[0]
if pattern.match(string)
  puts "Match found: #{pattern.match(string)}"
else
  puts "No match found."
end
