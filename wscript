import os.path
import sys
import waflib.Scripting
from os.path import expanduser
from waflib.Configure import conf
from waflib.Build import BuildContext, CleanContext, InstallContext, UninstallContext

if ("WIN32" == sys.platform.upper()):
    pass
else:
    import wwlinux as wafwerks

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
    _configure(ctx)
    wafwerks.debug_specifics(ctx)
    print "--- Create release configuration ---"
    ctx.setenv('release')
    ctx.load('compiler_cxx')
    ctx.define(ctx.env.DEST_OS.upper(), 1)
    _configure(ctx)
    wafwerks.release_specifics(ctx)

def _configure(ctx):
    ctx.env.INCLUDES = wafwerks.get_includes(ctx)
    ctx.env.LINKFLAGS = wafwerks.get_link_flags(ctx)
    ctx.env.LIB = wafwerks.get_libs(ctx)
    ctx.env.LIBPATH = wafwerks.get_libs_path(ctx)
    ctx.env.STLIB = wafwerks.get_stlibs(ctx)
    ctx.env.STLIBPATH = wafwerks.get_stlibs_path(ctx)
    ctx.env.CXXFLAGS = wafwerks.get_cxx_flags(ctx)

def build(ctx):
    if not ctx.variant:
        msg = 'call "waf '+ ctx.cmd +'_debug" or "waf '+ ctx.cmd +'_release", and try "waf --help"'
        ctx.fatal(msg)
    app_name = APPNAME
    if ctx.variant == 'debug':
        app_name = APPNAME + '.debug'
    if ctx.cmd == 'clean_' + ctx.variant:
        ctx.exec_command('rm -f %s' % (app_name))
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

