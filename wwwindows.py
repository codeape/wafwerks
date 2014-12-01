import os.path

def get_includes(ctx):
    ldw = ctx.options.leadwerks_path
    print(ctx.env.INCLUDES)
    includes = ctx.env.INCLUDES + ['.',
                os.path.join(ldw, 'Include'),
                os.path.join(ldw, 'Include', 'Libraries', 'freetype-2.4.7', 'include'),
                os.path.join(ldw, 'Include', 'Libraries', 'OpenAL', 'include'),
                os.path.join(ldw, 'Include', 'Libraries', 'NewtonDynamics', 'packages', 'dMath'),
                os.path.join(ldw, 'Include', 'Libraries', 'NewtonDynamics', 'packages', 'thirdParty', 'pthreads.2'),
                os.path.join(ldw, 'Include', 'Libraries', 'NewtonDynamics', 'packages', 'dContainers'),
                os.path.join(ldw, 'Include', 'Libraries', 'NewtonDynamics', 'packages', 'dCustomJoints'),
                os.path.join(ldw, 'Include', 'Libraries', 'NewtonDynamics', 'coreLibrary_300', 'source', 'openCL'),
                os.path.join(ldw, 'Include', 'Libraries', 'NewtonDynamics', 'coreLibrary_300', 'source', 'core'),
                os.path.join(ldw, 'Include', 'Libraries', 'NewtonDynamics', 'coreLibrary_300', 'source', 'meshUtil'),
                os.path.join(ldw, 'Include', 'Libraries', 'NewtonDynamics', 'coreLibrary_300', 'source', 'physics'),
                os.path.join(ldw, 'Include', 'Libraries', 'RecastNavigation', 'RecastDemo', 'Include'),
                os.path.join(ldw, 'Include', 'Libraries', 'RecastNavigation', 'DetourCrowd', 'Include'),
                os.path.join(ldw, 'Include', 'Libraries', 'RecastNavigation', 'DetourTileCache', 'Include'),
                os.path.join(ldw, 'Include', 'Libraries', 'RecastNavigation', 'DebugUtils', 'Include'),
                os.path.join(ldw, 'Include', 'Libraries', 'RecastNavigation', 'Recast', 'Include'),
                os.path.join(ldw, 'Include', 'Libraries', 'NewtonDynamics', 'coreLibrary_300', 'source', 'newton'),
                os.path.join(ldw, 'Include', 'Libraries', 'RecastNavigation', 'Detour', 'Include'),
                os.path.join(ldw, 'Include', 'Libraries', 'tolua++-1.0.93', 'include'),
                os.path.join(ldw, 'Include', 'Libraries', 'lua-5.1.4'),
                os.path.join(ldw, 'Include', 'Libraries', 'glew-1.6.0', 'include' ,'GL'),
                os.path.join(ldw, 'Include', 'Libraries', 'glew-1.6.0', 'include'),
                os.path.join(ldw, 'Include', 'Libraries', 'enet-1.3.1', 'include'),
                os.path.join(ldw, 'Include', 'Libraries', 'zlib-1.2.5'),
                os.path.join(ldw, 'Include', 'Libraries', 'freetype-2.4.3', 'include')]
    return includes

def get_link_flags(ctx):
    return ['/MANIFEST',
            '/NXCOMPAT',
            '/DYNAMICBASE',
            '/MACHINE:X86',
            '/SAFESEH',
            '/SUBSYSTEM:CONSOLE',
            '/MANIFESTUAC:"level=\'asInvoker\' uiAccess=\'false\'"',
            '/ERRORREPORT:PROMPT',
            '/NOLOGO',
            '/TLBID:1',
            '/NODEFAULTLIB:MSVCRT.lib']

def get_libs(ctx):
    return []

def get_libs_path(ctx):
    return []

def get_stlibs(ctx):
    return ["Leadwerks.lib",
            "lua51.lib",
            "steam_api.lib",
            "ws2_32.lib",
            "OpenGL32.lib",
            "Glu32.lib",
            "winmm.lib",
            "Psapi.lib",
            "OpenAL32.lib",
            "kernel32.lib",
            "user32.lib",
            "gdi32.lib",
            "winspool.lib",
            "comdlg32.lib",
            "advapi32.lib",
            "shell32.lib",
            "ole32.lib",
            "oleaut32.lib",
            "uuid.lib",
            "odbc32.lib",
            "odbccp32.lib"]

def get_stlibs_path(ctx):
    ldw = ctx.options.leadwerks_path
    return [os.path.join(ldw, 'Library', 'Windows', 'x86')]

def get_cxx_flags(ctx):
    cxx_flags = ['/GS',
                 '/analyze-',
                 '/W3',
                 '/Zc:wchar_t',
                 '/Zi',
                 '/Gm',
                 '/Od',
                 '/fp:precise',
                 '/D "PSAPI_VERSION=1"',
                 '/D "__STEAM__"',
                 '/D "_CUSTOM_JOINTS_STATIC_LIB"',
                 '/D "FT2_BUILD_LIBRARY"',
                 '/D "LEADWERKS_3_1"',
                 '/D "DG_DISABLE_ASSERT"',
                 '/D "WINDOWS"',
                 '/D "WIN32"',
                 '/D "OS_WINDOWS"',
                 '/D "OPENGL"',
                 '/D "PLATFORM_WINDOWS"',
                 '/D "_WIN_32_VER"',
                 '/D "_NEWTON_USE_LIB"',
                 '/D "PTW32_STATIC_LIB"',
                 '/D "PTW32_BUILD"',
                 '/D "_NEWTON_STATIC_LIB"',
                 '/D "_LIB"',
                 '/D "DG_USE_NORMAL_PRIORITY_THREAD"',
                 '/D "GLEW_STATIC"',
                 '/D "_STATICLIB"',
                 '/errorReport:prompt',
                 '/WX-',
                 '/Zc:forScope',
                 '/Gd',
                 '/Oy-',
                 '/EHsc',
                 '/nologo',
                 '/D "SLB_LIBRARY"']
    return cxx_flags

def debug_specifics(ctx):
    ldw = ctx.options.leadwerks_path
    ctx.env.prepend_value('CXXFLAGS', ['/Fd"'+ os.path.join('Debug','vc120.pdb') + '"',
                                       '/D "DEBUG"',
                                       '/D "_DEBUG"',
                                       '/MTd',
                                       '/Fa"Debug\\"',
                                       #'/Fo"Debug\\"',
                                       '/Fp"'+os.path.join('Debug','wafwerks.debug.pch')+'"'])
    ctx.env.prepend_value('LINKFLAGS', ['/DEBUG', '/INCREMENTAL', '/NODEFAULTLIB:MSVCRTD.lib'
                                        '/PDB:"C:\\Users\\eoscnor\\Documents\\Leadwerks\\Projects\\wafwerks\\build\\debug\\wafwerks.debug.pdb"',
                                        '/PGD:"C:\\Users\\eoscnor\\Documents\\Leadwerks\\Projects\\wafwerks\\build\\debug\\wafwerks.debug.pgd"',
                                        '/ManifestFile:"build\\Debug\\wafwerks.debug.exe.intermediate.manifest"'])
    ctx.env.prepend_value('LIBPATH', [os.path.join(ldw, 'Library', 'Windows', 'x86', 'Debug')])
    #/PDB:"C:\Users\eoscnor\Documents\Leadwerks\Projects\wafwerks\Projects\Windows\..\..\wafwerks.debug.pdb"
    #/PGD:"C:\Users\eoscnor\Documents\Leadwerks\Projects\wafwerks\Projects\Windows\..\..\wafwerks.debug.pgd"
    #/ManifestFile:"Debug\wafwerks.debug.exe.intermediate.manifest"
    #/LIBPATH:"C:/Program Files (x86)/Steam/steamapps/common/Leadwerks\Library\Windows\x86\Debug"
    #/LIBPATH:"C:/Program Files (x86)/Steam/steamapps/common/Leadwerks\Library\Windows\x86" 

def release_specifics(ctx):
    ldw = ctx.options.leadwerks_path
    ctx.env.prepend_value('INCLUDES', [os.path.join(ldw, 'Include', 'Libraries', 'LuaJIT', 'dynasm'),
                                       os.path.join(ldw, 'Include', 'Libraries', 'LuaJIT', 'src')])
    ctx.env.prepend_value('CXXFLAGS', ['/Gy',
                                       '/Fd"'+ os.path.join('Release','vc120.pdb') + '"',
                                       '/Oi',
                                       '/MT',
                                       '/Fa"Release\\"',
                                       #'/Fo"Release\\"',
                                       '/Fp"'+os.path.join('Release','wafwerks.pch')+'"',
                                       '/MP'])
    ctx.env.prepend_value('LINKFLAGS', ['/LTCG', '/OPT:REF', '/INCREMENTAL:NO', '/OPT:ICF',
                          '/PDB:"C:\\Users\\eoscnor\\Documents\\Leadwerks\\Projects\\wafwerks\\build\\release\\wafwerks.pdb"',
                          '/PGD:"C:\\Users\\eoscnor\\Documents\\Leadwerks\\Projects\\wafwerks\\build\\release\\wafwerks.pgd"',
                          '/ManifestFile:"Release\\wafwerks.exe.intermediate.manifest"'])
    ctx.env.prepend_value('LIBPATH', [os.path.join(ldw, 'Library', 'Windows', 'x86', 'Release')])
    #/PDB:"C:\Users\eoscnor\Documents\Leadwerks\Projects\wafwerks\Projects\Windows\..\..\wafwerks.pdb"
    #/PGD:"C:\Users\eoscnor\Documents\Leadwerks\Projects\wafwerks\Projects\Windows\..\..\wafwerks.pgd"
    #/ManifestFile:"Release\wafwerks.exe.intermediate.manifest"
    #/LIBPATH:"C:/Program Files (x86)/Steam/steamapps/common/Leadwerks\Library\Windows\x86"
    #/LIBPATH:"C:/Program Files (x86)/Steam/steamapps/common/Leadwerks\Library\Windows\x86\Release"
    #/LIBPATH:"C:/Leadwerks\Engine\Source\Libraries\OpenAL/libs/Win32/EFX-Util_MT"
    #/LIBPATH:"C:/Leadwerks\Engine\Source\Libraries\OpenAL/libs/Win32" 

#/MANIFEST /NXCOMPAT  /DYNAMICBASE "Leadwerks.lib" "lua51.lib" "steam_api.lib" "ws2_32.lib" "OpenGL32.lib" "Glu32.lib" "winmm.lib" "Psapi.lib" "OpenAL32.lib" "kernel32.lib" "user32.lib" "gdi32.lib" "winspool.lib" "comdlg32.lib" "advapi32.lib" "shell32.lib" "ole32.lib" "oleaut32.lib" "uuid.lib" "odbc32.lib" "odbccp32.lib"  /MACHINE:X86 /SAFESEH /SUBSYSTEM:CONSOLE /MANIFESTUAC:"level='asInvoker' uiAccess='false'"  /ERRORREPORT:PROMPT /NOLOGO /TLBID:1 
#/MANIFEST /NXCOMPAT  /DYNAMICBASE "Leadwerks.lib" "lua51.lib" "steam_api.lib" "ws2_32.lib" "OpenGL32.lib" "Glu32.lib" "winmm.lib" "Psapi.lib" "OpenAL32.lib" "kernel32.lib" "user32.lib" "gdi32.lib" "winspool.lib" "comdlg32.lib" "advapi32.lib" "shell32.lib" "ole32.lib" "oleaut32.lib" "uuid.lib" "odbc32.lib" "odbccp32.lib"  /MACHINE:X86 /SAFESEH /SUBSYSTEM:CONSOLE /MANIFESTUAC:"level='asInvoker' uiAccess='false'"  /ERRORREPORT:PROMPT /NOLOGO /TLBID:1 