import os.path

def get_includes(ctx):
    ldw = ctx.options.leadwerks_path
    includes = ['.',
                os.path.join(ldw, 'Include'),
                os.path.join(ldw, 'Include/Libraries/VHACD/src/VHACD_Lib/inc'),
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
    return includes

def get_link_flags(ctx):
    return ['-Wl,-rpath=$ORIGIN']

def get_libs(ctx):
    return ['openal',
            'GL',
            'GLU',
            'X11',
            'pthread',
            'steam_api',
            'dl']

def get_libs_path(ctx):
    return [os.path.join('/usr','lib'), ctx.top_dir]

def get_stlibs(ctx):
    return [':libluajit.a', ':Leadwerks.a']

def get_stlibs_path(ctx):
    ldw = ctx.options.leadwerks_path
    return [os.path.join('/usr','lib'),
            os.path.join(ldw, 'Library', 'Linux'),
            os.path.join(ldw, 'Library', 'Linux', 'Release')]

def get_cxx_flags(ctx):
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
    return cxx_flags

def debug_specifics(ctx):
    ctx.env.prepend_value('CXXFLAGS', ['-g', '-DDEBUG', '-D_DEBUG'])

def release_specifics(ctx):
    ctx.env.prepend_value('CXXFLAGS', ['-O2'])
    ctx.env.prepend_value('LINKFLAGS', ['-s'])

