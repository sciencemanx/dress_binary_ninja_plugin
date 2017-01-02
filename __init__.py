from binaryninja import *

def function_syms(bv):
	fmt = '{}() @ *0x{:x}'
	fs = [sym for k,sym in bv.symbols if sym.type == 'FunctionSymbol']
	return '\n'.join(fmt.format(f.name, f.address) for f in fs)

def global_syms(bv):
	fmt = "{} @ *0x{:x}"
	syms = [sym for k,sym in bv.symbols if sym.type == 'DataSymbol']
	return '\n'.join(fmt.format(sym.name, sym.address) for sym in syms)

def get_symbols(bv):
	show_plain_text_report('.syms', '\n'.join([function_syms(bv), global_syms(bv)]))
  
PluginCommand.register('Export Symbols', 'Export symbols to dress format', get_symbols)