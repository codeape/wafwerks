import os.path
from os.path import expanduser
import sys
from waflib.Configure import conf
import waflib.Scripting
from waflib.Build import BuildContext, CleanContext, InstallContext, UninstallContext

APPNAME = 'project-name'
VERSION = '0.0.1'

SRCFILES = [os.path.join('Source', 'App.cpp'),
            os.path.join('Source', 'main.cpp')]

top = '.'
out = 'build'

@conf
def libckok (ctx, libname, libpath):
    ctx.check(header_name=libpath, features='cxx cprogram',
              okmsg="{0} is present".format(libname),
              errmsg="{0} is not present".format(libname))

def options(opt):
    opt.load('compiler_cxx')
    if ("WIN32" == sys.platform.upper()):
        lw_path = 'unknown'
    else:
        lw_path = home = os.path.join(expanduser('~'),
                                      '.steam/steam/SteamApps/common/Leadwerks')

    opt.add_option('--leadwerks-lib', action='store', dest='leadwerks_path',
                   default=lw_path)

def configure(ctx):
    print "--- Create debug configuration ---"
    ctx.setenv('debug')
    ctx.load('compiler_cxx')
    ctx.define(ctx.env.DEST_OS.upper(), 1)
    if ("WIN32" == ctx.env.DEST_OS.upper()):
        _configure_win(ctx)
    else:
        _configure_linux(ctx)
        ctx.env.prepend_value('CXXFLAGS', ['-g', '-DDEBUG', '-D_DEBUG'])
    print "--- Create release configuration ---"
    ctx.setenv('release')
    ctx.load('compiler_cxx')
    ctx.define(ctx.env.DEST_OS.upper(), 1)
    if ("WIN32" == ctx.env.DEST_OS.upper()):
        _configure_win(ctx)
    else:
        _configure_linux(ctx)
        ctx.env.prepend_value('CXXFLAGS', ['-O2'])
        ctx.env.prepend_value('LINKFLAGS', ['-s'])


def _configure_win(ctx):
    pass

def _configure_linux(ctx):
    ldw = ctx.options.leadwerks_path
    includes = ['.',
                os.path.join(ldw, 'Include'),
                os.path.join(ldw, 'Include/Libraries/NewtonDynamics/coreLibrary_300/source/core'),
                os.path.join(ldw, 'Include/Libraries/NewtonDynamics/coreLibrary_300/source/meshUtil'),
                os.path.join(ldw, 'Include/Libraries/NewtonDynamics/coreLibrary_300/source/newton'),
                os.path.join(ldw, 'Include/Libraries/NewtonDynamics/coreLibrary_300/source/physics'),
                os.path.join(ldw, 'Include/Libraries/NewtonDynamics/packages/dMath'),
                os.path.join(ldw, 'Include/Libraries/NewtonDynamics/packages/dContainers'),
                os.path.join(ldw, 'Include/Libraries/NewtonDynamics/packages/dCustomJoints'),
                os.path.join(ldw, 'Include/Libraries/tolua++-1.0.93/include'),
                os.path.join(ldw, 'Include/Libraries/lua-5.1.4'),
                os.path.join(ldw, 'Include/Libraries/freetype-2.4.7/include'),
                os.path.join(ldw, 'Include/Libraries/enet-1.3.1/include'),
                os.path.join(ldw, 'Include/Libraries/RecastNavigation/DebugUtils/Include'),
                os.path.join(ldw, 'Include/Libraries/RecastNavigation/Detour/Include'),
                os.path.join(ldw, 'Include/Libraries/RecastNavigation/DetourCrowd/Include'),
                os.path.join(ldw, 'Include/Libraries/RecastNavigation/DetourTileCache/Include'),
                os.path.join(ldw, 'Include/Libraries/RecastNavigation/Recast/Include'),
                os.path.join(ldw, 'Include/Libraries/zlib-1.2.5'),
                os.path.join(ldw, 'Include/Libraries/zlib-1.2.5/contrib/minizip'),
                os.path.join(ldw, 'Include/Libraries/freetype-2.4.7/include/freetype'),
                os.path.join(ldw, 'Include/Libraries/freetype-2.4.7/include/freetype/config'),
                os.path.join(ldw, 'Include/Libraries/LuaJIT/dynasm'),
                os.path.join(ldw, 'Include/Libraries/glew-1.6.0/include')]
    link_flags = ['-Wl,-rpath=$ORIGIN']
    libs = ['openal',
            'GL',
            'GLU',
            'X11',
            'pthread',
            'steam_api',
            'dl']
    libs_path = [os.path.join('/usr','lib'), ctx.top_dir]
    stlibs = [':libluajit.a', ':Leadwerks.a']
    stlibspath = [
                    os.path.join('/usr','lib'),
                    os.path.join(ldw, 'Library', 'Linux'),
                    os.path.join(ldw, 'Library', 'Linux', 'Release')
                ]
    cxx_flags = ['-Wall',
                 '-fexceptions',
                 '-msse3',
                 '-Wno-unknown-pragmas',
                 '-DDG_DISABLE_ASSERT',
                 '-DZLIB',
                 '-DPLATFORM_LINUX',
                 '-D_NEWTON_STATIC_LIB',
                 '-DFT2_BUILD_LIBRARY',
                 '-DOPENGL',
                 '-Dunix',
                 '-D__STEAM__',
                 '-D_POSIX_VER',
                 '-D_POSIX_VER_64',
                 '-DDG_THREAD_EMULATION',
                 '-D_STATICLIB',
                 '-DDG_USE_THREAD_EMULATION',
                 '-DGL_GLEXT_PROTOTYPES',
                 '-DLEADWERKS_3_1',
                 '-DLUA_USE_LINUX',
                 '-D_CUSTOM_JOINTS_STATIC_LIB']
    ctx.env.INCLUDES = includes
    ctx.env.LINKFLAGS = link_flags
    ctx.env.LIB = libs
    ctx.env.LIBPATH = libs_path
    ctx.env.STLIB = stlibs
    ctx.env.STLIBPATH = stlibspath
    ctx.env.CXXFLAGS = cxx_flags

def build(ctx):
    if not ctx.variant:
        msg = 'call "waf '+ ctx.cmd +'_debug" or "waf '+ ctx.cmd +'_release", and try "waf --help"'
        ctx.fatal(msg)
    app_name = APPNAME
    if ctx.cmd == 'clean_' + ctx.variant:
        ctx.exec_command('rm -f %s' % (app_name))
    if ctx.variant == 'debug':
        app_name = APPNAME + '.debug'
    ctx.program(source=SRCFILES, target=os.path.join('..', '..', app_name))

def distclean(ctx):
    waflib.Scripting.distclean(ctx)
    ctx.exec_command('rm -f %s %s' % (APPNAME, APPNAME + '.debug'))

for x in ['debug', 'release']:
    for y in (BuildContext, CleanContext, InstallContext, UninstallContext):
        name = y.__name__.replace('Context','').lower()
        class tmp(y):
            cmd = name + '_' + x
            variant = x

