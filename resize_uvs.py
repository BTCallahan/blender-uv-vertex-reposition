#Brian Callahan, 2/26/2018
import bpy

# will finish later
class UV_Panel(bpy.types.Panel):
    bl_label = "Resize UVs"
    #bl_idname = "OBJECT_PT_bento_rigging"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Rescale UVs'
    #bl_context = "create"
    bl_options = {'DEFAULT_CLOSED'}



class ResizeUV(bpy.types.Operator):
    
    
    bl_idname = 'object.resize_uv'
    bl_label = 'Resize UVs'
    
    @classmethod
    def poll(cls, context):
        for o in contest.selected_objects:
            if o.type == 'MESH':
                return True
        return False
    
    def execute(self, context):
        
        return {'FINISHED'}
        

def resizeUV(formerVYpixSize, pixelsAddedToTop, pixelsAddedToBottom, formerUXpixSize, pixelsAddedToRight, pixelsAddedToLeft, uvLayerNameNo=0, materialName=''):
    
    obs = bpy.context.selected_objects
    #256, 64, 128, 256, 0, 0, 0
    def addUp(start, addToTop, addToBottom, value):#256, 64, 128, 0.5
        
        
        oldPixPos = value * start#0.5 * 256 = 128
        
        newPixPos = oldPixPos + addToTop#128 + 64 = 192
        
        total = start + addToTop + addToBottom#256 + 64 + 128 = 448 
        
        try:
            return newPixPos / total#192 / 448 = 0.42857142857
        except ZeroDivisionError:
            return value
        
    def checkdata(data, name):
        
        if len(data.materials) > 0:
            
            for m in data.materials:
                
                if m.name != name:
                    return False
            return True
        return False
    
    modifiedDataNames = set()
    
    for o in obs:
        
        if o.type == 'MESH' and checkdata(o.data, materialName) and o.data.name not in modifiedDataNames:
            
            errors = False
            
            try:
                uvLayer = o.data.uv_layers[uvLayerNameNo]
            except IndexError:
                if len(o.data.uv_layers) < 1:
                    errors = True
                elif uvLayerNameNo < 0:
                    uvLayer = o.data.uv_layers[0]
                else:
                    uvLayer = o.data.uv_layers[-1]
            
            if not errors:
                for u in uvLayer.data:
                    
                    u.uv[0] = addUp(formerUXpixSize, pixelsAddedToRight, pixelsAddedToLeft, u.uv[0])
                    u.uv[1] = addUp(formerVYpixSize, pixelsAddedToTop, pixelsAddedToBottom, u.uv[1])
                    
                    modifiedDataNames.add(o.data.name)
                    print('Succeded')
                    #print("Current Y: {0:3}, diffrence size: {1}, percentage diffrence: {2:3}, new percentage diffrence: {3:3}, new uv Y: {4:3}".format(Y, dif, difPercent, newPewrcent, u.uv[1]))


resizeUV(256, 256, 0, 256, 0, 0, 0, 'Level3Static')
"""
def register():
    bpy.utils.register_class(ResizeUV)

def unregister():
    bpy.utils.unregister_class(ResizeUV)

if __name__ == '__main__':
    register()
"""
    