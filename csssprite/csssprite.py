#!/usr/bin/env python

"""
	csssprite.py
	Kailash Nadh, http://nadh.in
	June 2013
	
	http://github.com/knadh/csssprite	
	License: GPL v2
"""

import argparse
import os, Image, re

class CSSsprite:
	"""A simple class for merging images into a sprite with accompanying css"""

	def __init__(self, src_dir="./", target_dir="./"):
		"""Initialize with input and output directory paths"""
		self.src_dir = os.path.normpath(src_dir) + os.sep
		self.target_dir = os.path.normpath(target_dir) + os.sep

	def generate(self, filetype="png", name="sprite", orientation="vertical", spacing=30):
		"""Generate the sprite and the css file"""

		# image files
		files = self._get_files(self.src_dir, filetype)

		if not files:
			return 0

		total_height = 0
		max_height = 0

		total_width = 0
		max_width = 0

		# figure out the maximum combined dimensions of all images
		for filename in files:
			img = Image.open(self.src_dir + filename)
			width, height = img.size
			
			total_height += height + spacing
			max_height = height if height > max_height else max_height

			total_width += width + spacing
			max_width = width if width > max_width else max_width

		if orientation is "vertical":
			spr = Image.new( "RGBA", [max_width, total_height] )
		else:
			spr = Image.new( "RGBA", [total_width, max_height] )

		distance = 0
		css_lines = []
		for filename in files:
			img = Image.open(self.src_dir + filename)
			width, height = img.size
			
			if orientation == "vertical":
				line = "#%s .%s { background-position: 5px -%spx; }"
			else:
				line = "#%s .%s { background-position: %spx 5px; }"
			
			classname = filename.lower().replace("." + filetype, "")
			classname = re.sub(r"[^a-z0-9_\-]", "", classname)

			css_lines.append( line % (name, classname, distance) )
			
			if orientation is "vertical":
				spr.paste(img, (0, distance))
				distance += height + spacing
			else:
				spr.paste(img, (distance, 0))
				distance += width + spacing

		# save the sprite image
		spr.save( self.target_dir + name + "." + filetype)
		
		try:
			css = open( name + ".css", "w")
			css.write( "\n".join(css_lines) )
			css.close()
		except:
			print("Failed to write the css file")
			raise

		return len(files)


	def _get_files(self, src_dir, filetype):
		"""Get the list of image files in a directory"""

		try:
			directory = os.walk(src_dir)
		except:
			print("Error opening input directory")
			raise

		files = []
		for dirname, dirnames, filenames in directory:
			for filename in filenames:
				filename = filename.lower()
				if  filename.find('.' + filetype) != -1:
					files.append(filename)

		return files

# ===

# console entry
def main():
	print """csssprite by Kailash Nadh (http://nadh.in)
	--help for help

	"""

	# parse arguments
	parser = argparse.ArgumentParser(description='Generate an image+css sprite from multiple images')
	parser.add_argument('--in', dest='src_dir', required=True, help='path to directory containing images')
	parser.add_argument('--out', dest='target_dir', required=True, help='path to the directory where image+css should be generated')
	parser.add_argument('--name', dest='name', default='sprite', help='name of the output image and layer id in the css (default=sprite)')
	parser.add_argument('--orientation', dest='orientation', default='vertical', help='orientation of sprites. horizontal or vertical (default)')
	parser.add_argument('--spacing', dest='spacing', default=30, help='distance between individual tiles (default=30)')
	parser.add_argument('--filetype', dest='filetype', default="png", help='image filetype (default=png)')

	args = parser.parse_args()

	sprite = CSSsprite(args.src_dir, args.target_dir)
	num = sprite.generate(name=args.name, filetype=args.filetype, orientation=args.orientation, spacing=args.spacing)

	print "> Merged %s images into %s.%s" % (num, args.name, args.filetype)
	print "> CSS definitions written to %s.css" % args.name

if __name__ == '__main__':
	main()
