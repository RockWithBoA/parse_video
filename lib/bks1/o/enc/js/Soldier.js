/* Soldier.js, parse_video/lib/bks1/o/enc
 * last_update 2015-08-20 22:09 GMT+0800 CST
 */

// package com.qiyi.player.core.video.engine.dispatcher
// import flash.utils.getDefinitionByName;

// public class Soldier extends Object
	
// private static var _food:Object;
var _food = null;
	
// public static function set food(param1:Object) : void
	// NOTE this function is no use
	function set_food(param1) {
		if (_food == null) {
			_food = param1;
			fight();
		}
	}

// private static function fight() : void
	function fight(_dota) {
		
		// var _loc1:Object = getDefinitionByName(String.fromCharCode(99,111,109,46,113,105,121,105,46,112,108,97,121,101,114,46,99,111,114,101,46,118,105,100,101,111,46,101,110,103,105,110,101,46,100,109,46,112,114,111,118,105,100,101,114,46,77,101,100,105,97,68,111,116,97));
		// var _loc2:Object = new _loc1();
		
		// NOTE 'com.qiyi.player.core.video.engine.dm.provider.MediaDota'
		var _loc2 = _dota;	// NOTE this should be MediaDota
		
		// NOTE gen main data
		var _loc3 = String.fromCharCode(102,57,56,99,57,53,54,54,51,55,97,57,57,55,56,55,98,100,49,57,55,101,97,99,100,55,55,97,99,99,101,53,101);
		_loc2[_loc3](_loc2[String.fromCharCode(102,48,49,50,48,97,52,102,57,49,57,54,97,53,102,57,101,98,57,102,53,50,51,102,51,49,102,57,49,52,100,97,55)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,52,57,48,98,50,56,51,52,101,54,53,55,51,55,99,49,102,99,101,57,53,101,52,54,56,99,99,56,98,56,98,102)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,53,49,100,52,98,53,56,49,100,50,49,99,50,48,97,49,54,49,52,55,98,49,55,99,51,97,100,99,55,56,54,55)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,54,97,48,99,102,54,101,100,102,50,48,48,54,48,51,52,52,98,52,54,53,55,48,54,98,54,49,55,49,57,97,97)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,57,55,98,50,102,49,101,100,102,54,52,48,53,56,48,102,54,54,48,53,54,99,99,52,98,102,99,102,54,51,51,53)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,53,52,101,53,100,52,102,52,48,56,99,98,99,51,97,102,55,52,98,55,53,54,101,97,101,97,50,102,97,49,57,57)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,48,52,52,57,57,48,52,102,98,102,51,50,54,48,55,98,102,56,99,101,53,99,50,54,56,50,51,100,98,99,50,57)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,53,56,52,57,50,53,51,99,48,99,48,55,102,56,56,57,52,99,57,102,102,50,101,53,98,54,57,101,56,51,52,97)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,97,98,48,102,100,51,54,49,102,100,101,53,99,51,54,50,53,102,101,55,54,48,48,55,102,50,48,52,99,99,48,52)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,101,53,50,57,97,57,99,101,97,52,97,55,50,56,101,98,57,99,53,56,50,56,98,49,51,98,50,50,56,52,52,99)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,48,100,52,55,98,56,51,52,54,100,53,55,98,49,50,97,53,56,48,55,99,51,54,102,98,49,102,49,52,102,51,99)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,102,102,55,56,54,52,56,98,101,53,50,97,52,101,55,57,53,49,51,102,52,101,55,48,98,50,54,54,99,54,50,97)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,54,50,50,54,102,55,99,98,101,53,57,101,57,57,97,57,48,98,53,99,101,102,54,102,57,52,102,57,54,54,102,100)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,53,54,57,101,102,55,50,54,52,50,98,101,48,102,97,100,100,55,49,49,100,54,97,52,54,56,100,54,56,101,101,49)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,57,102,98,99,100,55,100,99,101,53,101,51,102,51,51,52,99,97,54,49,100,97,101,54,97,100,53,55,52,49,53,97)]);
		_loc2[_loc3](_loc2[String.fromCharCode(102,57,97,98,99,100,101,51,99,53,56,52,54,50,56,97,48,50,54,50,48,98,102,55,57,54,100,101,101,49,50,48,52)]);
		
		// _food[String.fromCharCode(116,104,100)] = _loc2;
		// NOTE 'thd'
		// NOTE _loc2 is thd
		// NOTE not set, just return the result
		return _loc2;
	}

// function add for easy
	function get_thd(_dota) {
		return fight(_dota);
	}

// try to export for node.js
try {
	exports.get_thd = get_thd;	// get_thd(_dota);
} catch (e) {
}	// nothing to do if exports failed

/* end Soldier.js */

