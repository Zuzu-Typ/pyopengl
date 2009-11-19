'''OpenGL extension NV.geometry_program4

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_geometry_program4'
_DEPRECATED = False
GL_LINES_ADJACENCY_EXT = constant.Constant( 'GL_LINES_ADJACENCY_EXT', 0xA )
GL_LINE_STRIP_ADJACENCY_EXT = constant.Constant( 'GL_LINE_STRIP_ADJACENCY_EXT', 0xB )
GL_TRIANGLES_ADJACENCY_EXT = constant.Constant( 'GL_TRIANGLES_ADJACENCY_EXT', 0xC )
GL_TRIANGLE_STRIP_ADJACENCY_EXT = constant.Constant( 'GL_TRIANGLE_STRIP_ADJACENCY_EXT', 0xD )
GL_GEOMETRY_PROGRAM_NV = constant.Constant( 'GL_GEOMETRY_PROGRAM_NV', 0x8C26 )
GL_MAX_PROGRAM_OUTPUT_VERTICES_NV = constant.Constant( 'GL_MAX_PROGRAM_OUTPUT_VERTICES_NV', 0x8C27 )
GL_MAX_PROGRAM_TOTAL_OUTPUT_COMPONENTS_NV = constant.Constant( 'GL_MAX_PROGRAM_TOTAL_OUTPUT_COMPONENTS_NV', 0x8C28 )
GL_GEOMETRY_VERTICES_OUT_EXT = constant.Constant( 'GL_GEOMETRY_VERTICES_OUT_EXT', 0x8DDA )
GL_GEOMETRY_INPUT_TYPE_EXT = constant.Constant( 'GL_GEOMETRY_INPUT_TYPE_EXT', 0x8DDB )
GL_GEOMETRY_OUTPUT_TYPE_EXT = constant.Constant( 'GL_GEOMETRY_OUTPUT_TYPE_EXT', 0x8DDC )
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT = constant.Constant( 'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT', 0x8C29 )
glget.addGLGetConstant( GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT, (1,) )
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT = constant.Constant( 'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT', 0x8DA7 )
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT', 0x8DA8 )
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT', 0x8DA9 )
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT = constant.Constant( 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT', 0x8CD4 )
GL_PROGRAM_POINT_SIZE_EXT = constant.Constant( 'GL_PROGRAM_POINT_SIZE_EXT', 0x8642 )
glget.addGLGetConstant( GL_PROGRAM_POINT_SIZE_EXT, (1,) )
glProgramVertexLimitNV = platform.createExtensionFunction( 
'glProgramVertexLimitNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,),
doc='glProgramVertexLimitNV(GLenum(target), GLint(limit)) -> None',
argNames=('target','limit',),
deprecated=_DEPRECATED,
)

glFramebufferTextureEXT = platform.createExtensionFunction( 
'glFramebufferTextureEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLuint,constants.GLint,),
doc='glFramebufferTextureEXT(GLenum(target), GLenum(attachment), GLuint(texture), GLint(level)) -> None',
argNames=('target','attachment','texture','level',),
deprecated=_DEPRECATED,
)

glFramebufferTextureLayerEXT = platform.createExtensionFunction( 
'glFramebufferTextureLayerEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLuint,constants.GLint,constants.GLint,),
doc='glFramebufferTextureLayerEXT(GLenum(target), GLenum(attachment), GLuint(texture), GLint(level), GLint(layer)) -> None',
argNames=('target','attachment','texture','level','layer',),
deprecated=_DEPRECATED,
)

glFramebufferTextureFaceEXT = platform.createExtensionFunction( 
'glFramebufferTextureFaceEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLuint,constants.GLint,constants.GLenum,),
doc='glFramebufferTextureFaceEXT(GLenum(target), GLenum(attachment), GLuint(texture), GLint(level), GLenum(face)) -> None',
argNames=('target','attachment','texture','level','face',),
deprecated=_DEPRECATED,
)


def glInitGeometryProgram4NV():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
