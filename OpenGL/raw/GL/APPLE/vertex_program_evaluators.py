'''OpenGL extension APPLE.vertex_program_evaluators

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_APPLE_vertex_program_evaluators'
_DEPRECATED = False
GL_VERTEX_ATTRIB_MAP1_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP1_APPLE', 0x8A00 )
GL_VERTEX_ATTRIB_MAP2_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP2_APPLE', 0x8A01 )
GL_VERTEX_ATTRIB_MAP1_SIZE_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP1_SIZE_APPLE', 0x8A02 )
GL_VERTEX_ATTRIB_MAP1_COEFF_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP1_COEFF_APPLE', 0x8A03 )
GL_VERTEX_ATTRIB_MAP1_ORDER_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP1_ORDER_APPLE', 0x8A04 )
GL_VERTEX_ATTRIB_MAP1_DOMAIN_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP1_DOMAIN_APPLE', 0x8A05 )
GL_VERTEX_ATTRIB_MAP2_SIZE_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP2_SIZE_APPLE', 0x8A06 )
GL_VERTEX_ATTRIB_MAP2_COEFF_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP2_COEFF_APPLE', 0x8A07 )
GL_VERTEX_ATTRIB_MAP2_ORDER_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP2_ORDER_APPLE', 0x8A08 )
GL_VERTEX_ATTRIB_MAP2_DOMAIN_APPLE = constant.Constant( 'GL_VERTEX_ATTRIB_MAP2_DOMAIN_APPLE', 0x8A09 )
glEnableVertexAttribAPPLE = platform.createExtensionFunction( 
'glEnableVertexAttribAPPLE',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,),
doc='glEnableVertexAttribAPPLE(GLuint(index), GLenum(pname)) -> None',
argNames=('index','pname',),
deprecated=_DEPRECATED,
)

glDisableVertexAttribAPPLE = platform.createExtensionFunction( 
'glDisableVertexAttribAPPLE',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,),
doc='glDisableVertexAttribAPPLE(GLuint(index), GLenum(pname)) -> None',
argNames=('index','pname',),
deprecated=_DEPRECATED,
)

glIsVertexAttribEnabledAPPLE = platform.createExtensionFunction( 
'glIsVertexAttribEnabledAPPLE',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLboolean, 
argTypes=(constants.GLuint,constants.GLenum,),
doc='glIsVertexAttribEnabledAPPLE(GLuint(index), GLenum(pname)) -> constants.GLboolean',
argNames=('index','pname',),
deprecated=_DEPRECATED,
)

glMapVertexAttrib1dAPPLE = platform.createExtensionFunction( 
'glMapVertexAttrib1dAPPLE',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLdouble,constants.GLdouble,constants.GLint,constants.GLint,arrays.GLdoubleArray,),
doc='glMapVertexAttrib1dAPPLE(GLuint(index), GLuint(size), GLdouble(u1), GLdouble(u2), GLint(stride), GLint(order), GLdoubleArray(points)) -> None',
argNames=('index','size','u1','u2','stride','order','points',),
deprecated=_DEPRECATED,
)

glMapVertexAttrib1fAPPLE = platform.createExtensionFunction( 
'glMapVertexAttrib1fAPPLE',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLfloat,constants.GLfloat,constants.GLint,constants.GLint,arrays.GLfloatArray,),
doc='glMapVertexAttrib1fAPPLE(GLuint(index), GLuint(size), GLfloat(u1), GLfloat(u2), GLint(stride), GLint(order), GLfloatArray(points)) -> None',
argNames=('index','size','u1','u2','stride','order','points',),
deprecated=_DEPRECATED,
)

glMapVertexAttrib2dAPPLE = platform.createExtensionFunction( 
'glMapVertexAttrib2dAPPLE',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLdouble,constants.GLdouble,constants.GLint,constants.GLint,constants.GLdouble,constants.GLdouble,constants.GLint,constants.GLint,arrays.GLdoubleArray,),
doc='glMapVertexAttrib2dAPPLE(GLuint(index), GLuint(size), GLdouble(u1), GLdouble(u2), GLint(ustride), GLint(uorder), GLdouble(v1), GLdouble(v2), GLint(vstride), GLint(vorder), GLdoubleArray(points)) -> None',
argNames=('index','size','u1','u2','ustride','uorder','v1','v2','vstride','vorder','points',),
deprecated=_DEPRECATED,
)

glMapVertexAttrib2fAPPLE = platform.createExtensionFunction( 
'glMapVertexAttrib2fAPPLE',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLfloat,constants.GLfloat,constants.GLint,constants.GLint,constants.GLfloat,constants.GLfloat,constants.GLint,constants.GLint,arrays.GLfloatArray,),
doc='glMapVertexAttrib2fAPPLE(GLuint(index), GLuint(size), GLfloat(u1), GLfloat(u2), GLint(ustride), GLint(uorder), GLfloat(v1), GLfloat(v2), GLint(vstride), GLint(vorder), GLfloatArray(points)) -> None',
argNames=('index','size','u1','u2','ustride','uorder','v1','v2','vstride','vorder','points',),
deprecated=_DEPRECATED,
)


def glInitVertexProgramEvaluatorsAPPLE():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
