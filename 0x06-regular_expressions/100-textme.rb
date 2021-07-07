#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(?<SENDER>.*?)\] .*\[to:(?<RECEIVER>.*?)\] .*\[flags:(?<FLAGS>.*?)\].*/).join(",")
