#!/bin/python3

import sublist3r
import optparse
import sys

parser = optparse.OptionParser()
parser.add_option('-d', '--domain', dest='domain', help='Give to find SubDomain of', metavar='example.com')
parser.add_option('-s','--save', dest='save', help='Save output to File', metavar='output.txt', default='output.txt')
(options, arguments) = parser.parse_args()

domain = options.domain
save = options.save
print("Finding Sub Domains for : "+domain)
def subEnum():
	subdomains = sublist3r.main(domain,40,save, ports= None, silent= True, verbose= False, enable_bruteforce= False, engines=None)


if len(sys.argv) < 2 :
	print("Use : -h or --help for usage!!")
	sys.exit()
elif sys.argv[1] == '-d':
	subEnum()
else:
	print("Use : -h or --help for usage!!")
