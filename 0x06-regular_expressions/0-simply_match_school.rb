#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

str = ARGV[0]
if str.match?(/\bSchool\b/)
  puts "Match found: #{str}"
else
  puts "No match found"
end

