# blender-uv-vertex-reposition
Ever bben working with a several objects that share the same texture image, but ended up running out of space and having to change the texture size? Ever had to manually resize the uvs for each and every object? Now you don't have to. 

To use this script, enter the old image dimentions, then enter the number of pixels what were added to the top and bottom of the image file (using negitive numbers if pixels were subtracted), as well as entering numbers for the left and right sides. Finaly, enter the number of the uv map that will be affected. For example:

A 64 by 64 image is opened in an image editing program. The user adds 16 pixels to the bottom, and 8 to the right side. Then in Blender, the used selects all meshes that use the image as a texture and runs the script, making sure to enter the paramiters for the original size, pixels added/subtracted, and the uv layer number. Later on the user realised that they ended up add more pixels that were needed to the bottom of the image. (wip)
