import os.path
import sys
import waflib.Scripting
from os.path import expanduser
from waflib.Configure import conf
from waflib.Build import BuildContext, CleanContext, InstallContext, UninstallContext

if ("WIN32" == sys.platform.upper()):
    import wwwindows as wafwerks
else:
    import wwlinux as wafwerks
import wwproject


APPNAME = wwproject.WWPROJECT_NAME
VERSION = wwproject.WWPROJECT_VERSION

top = '.'
out = 'build'

@conf
def libckok (ctx, libname, libpath):
    ctx.check(header_name=libpath, features='cxx cprogram',
              okmsg="{0} is present".format(libname),
              errmsg="{0} is not present".format(libname))

def options(opt):
    opt.load('compiler_cxx')
    if "WIN32" == sys.platform.upper():
        lw_path = 'C:\Program Files (x86)\Steam\SteamApps\common\Leadwerks'
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
    _configure(ctx)
    wafwerks.debug_specifics(ctx)
    print "--- Create release configuration ---"
    ctx.setenv('release')
    ctx.load('compiler_cxx')
    ctx.define(ctx.env.DEST_OS.upper(), 1)
    _configure(ctx)
    wafwerks.release_specifics(ctx)

def _configure(ctx):
    libs = wafwerks.get_libs(ctx)
    libs_path = wafwerks.get_libs_path(ctx)
    stlibs = wafwerks.get_stlibs(ctx)
    stlibs_path = wafwerks.get_stlibs_path(ctx)
    includes = wafwerks.get_includes(ctx)
    cxx_flags = wafwerks.get_cxx_flags(ctx)
    link_flags = wafwerks.get_link_flags(ctx)

    wwproject.configure(ctx,
                        libs,
                        libs_path,
                        stlibs,
                        stlibs_path,
                        includes,
                        cxx_flags,
                        link_flags)

    ctx.env.LIB = libs
    ctx.env.LIBPATH = libs_path
    ctx.env.STLIB = stlibs
    ctx.env.STLIBPATH = stlibs_path
    ctx.env.INCLUDES = includes
    ctx.env.CXXFLAGS = cxx_flags
    ctx.env.LINKFLAGS = link_flags

def build(ctx):
    if not ctx.variant:
        msg = 'call "waf '+ ctx.cmd +'_debug" or "waf '+ ctx.cmd +'_release", and try "waf --help"'
        ctx.fatal(msg)
    app_name = APPNAME
    if ctx.variant == 'debug':
        app_name = APPNAME + '.debug'
    if ctx.cmd == 'clean_' + ctx.variant:
        ctx.exec_command('rm -f %s' % (app_name))
    ctx.program(source=wwproject.src_files(ctx),
                target=os.path.join('..', '..', app_name))

def distclean(ctx):
    waflib.Scripting.distclean(ctx)
    ctx.exec_command('rm -f %s %s' % (APPNAME, APPNAME + '.debug'))

for x in ['debug', 'release']:
    for y in (BuildContext, CleanContext, InstallContext, UninstallContext):
        name = y.__name__.replace('Context','').lower()
        class tmp(y):
            cmd = name + '_' + x
            variant = x

