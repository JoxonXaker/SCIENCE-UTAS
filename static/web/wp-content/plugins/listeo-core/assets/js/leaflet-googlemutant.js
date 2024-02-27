(function(){"use strict";var NEWER=Symbol("newer");var OLDER=Symbol("older");var LRUMap=function LRUMap(limit,entries){if(typeof limit!=="number"){entries=limit;limit=0;}
this.size=0;this.limit=limit;this.oldest=this.newest=undefined;this._keymap=new Map();if(entries){this.assign(entries);if(limit<1){this.limit=this.size;}}};LRUMap.prototype._markEntryAsUsed=function _markEntryAsUsed(entry){if(entry===this.newest){return;}
if(entry[NEWER]){if(entry===this.oldest){this.oldest=entry[NEWER];}
entry[NEWER][OLDER]=entry[OLDER];}
if(entry[OLDER]){entry[OLDER][NEWER]=entry[NEWER];}
entry[NEWER]=undefined;entry[OLDER]=this.newest;if(this.newest){this.newest[NEWER]=entry;}
this.newest=entry;};LRUMap.prototype.assign=function assign(entries){var entry,limit=this.limit||Number.MAX_VALUE;this._keymap.clear();var it=entries[Symbol.iterator]();for(var itv=it.next();!itv.done;itv=it.next()){var e=new Entry(itv.value[0],itv.value[1]);this._keymap.set(e.key,e);if(!entry){this.oldest=e;}else{entry[NEWER]=e;e[OLDER]=entry;}
entry=e;if(limit--==0){throw new Error("overflow");}}
this.newest=entry;this.size=this._keymap.size;};LRUMap.prototype.get=function get(key){var entry=this._keymap.get(key);if(!entry){return;}
this._markEntryAsUsed(entry);return entry.value;};LRUMap.prototype.set=function set(key,value){var entry=this._keymap.get(key);if(entry){entry.value=value;this._markEntryAsUsed(entry);return this;}
this._keymap.set(key,(entry=new Entry(key,value)));if(this.newest){this.newest[NEWER]=entry;entry[OLDER]=this.newest;}else{this.oldest=entry;}
this.newest=entry;++this.size;if(this.size>this.limit){this.shift();}
return this;};LRUMap.prototype.shift=function shift(){var entry=this.oldest;if(entry){if(this.oldest[NEWER]){this.oldest=this.oldest[NEWER];this.oldest[OLDER]=undefined;}else{this.oldest=undefined;this.newest=undefined;}
entry[NEWER]=entry[OLDER]=undefined;this._keymap.delete(entry.key);--this.size;return[entry.key,entry.value];}};LRUMap.prototype.find=function find(key){var e=this._keymap.get(key);return e?e.value:undefined;};LRUMap.prototype.has=function has(key){return this._keymap.has(key);};LRUMap.prototype.delete=function delete$1(key){var entry=this._keymap.get(key);if(!entry){return;}
this._keymap.delete(entry.key);if(entry[NEWER]&&entry[OLDER]){entry[OLDER][NEWER]=entry[NEWER];entry[NEWER][OLDER]=entry[OLDER];}else if(entry[NEWER]){entry[NEWER][OLDER]=undefined;this.oldest=entry[NEWER];}else if(entry[OLDER]){entry[OLDER][NEWER]=undefined;this.newest=entry[OLDER];}else{this.oldest=this.newest=undefined;}
this.size--;return entry.value;};LRUMap.prototype.clear=function clear(){this.oldest=this.newest=undefined;this.size=0;this._keymap.clear();};LRUMap.prototype.keys=function keys(){return new KeyIterator(this.oldest);};LRUMap.prototype.values=function values(){return new ValueIterator(this.oldest);};LRUMap.prototype.entries=function entries(){return this;};LRUMap.prototype[Symbol.iterator]=function(){return new EntryIterator(this.oldest);};LRUMap.prototype.forEach=function forEach(fun,thisObj){if(typeof thisObj!=="object"){thisObj=this;}
var entry=this.oldest;while(entry){fun.call(thisObj,entry.value,entry.key,this);entry=entry[NEWER];}};LRUMap.prototype.toJSON=function toJSON(){var s=new Array(this.size),i=0,entry=this.oldest;while(entry){s[i++]={key:entry.key,value:entry.value};entry=entry[NEWER];}
return s;};LRUMap.prototype.toString=function toString(){var s="",entry=this.oldest;while(entry){s+=String(entry.key)+":"+entry.value;entry=entry[NEWER];if(entry){s+=" < ";}}
return s;};function Entry(key,value){this.key=key;this.value=value;this[NEWER]=undefined;this[OLDER]=undefined;}
function EntryIterator(oldestEntry){this.entry=oldestEntry;}
EntryIterator.prototype[Symbol.iterator]=function(){return this;};EntryIterator.prototype.next=function(){var ent=this.entry;if(ent){this.entry=ent[NEWER];return{done:false,value:[ent.key,ent.value]};}else{return{done:true,value:undefined};}};function KeyIterator(oldestEntry){this.entry=oldestEntry;}
KeyIterator.prototype[Symbol.iterator]=function(){return this;};KeyIterator.prototype.next=function(){var ent=this.entry;if(ent){this.entry=ent[NEWER];return{done:false,value:ent.key};}else{return{done:true,value:undefined};}};function ValueIterator(oldestEntry){this.entry=oldestEntry;}
ValueIterator.prototype[Symbol.iterator]=function(){return this;};ValueIterator.prototype.next=function(){var ent=this.entry;if(ent){this.entry=ent[NEWER];return{done:false,value:ent.value};}else{return{done:true,value:undefined};}};function waitForAPI(callback,context){var checkCounter=0,intervalId=null;intervalId=setInterval(function(){if(checkCounter>=20){clearInterval(intervalId);throw new Error("window.google not found after 10 seconds");}
if(!!window.google&&!!window.google.maps&&!!window.google.maps.Map){clearInterval(intervalId);callback.call(context);}
++checkCounter;},500);}
L.GridLayer.GoogleMutant=L.GridLayer.extend({options:{maxZoom:21,type:"roadmap",maxNativeZoom:21,},initialize:function(options){L.GridLayer.prototype.initialize.call(this,options);this._tileCallbacks={};this._lru=new LRUMap(100);this._imagesPerTile=this.options.type==="hybrid"?2:1;this._boundOnMutatedImage=this._onMutatedImage.bind(this);},onAdd:function(map){var this$1=this;L.GridLayer.prototype.onAdd.call(this,map);this._initMutantContainer();if(this._logoContainer){map._controlCorners.bottomleft.appendChild(this._logoContainer);}
if(this._attributionContainer){map._controlCorners.bottomright.appendChild(this._attributionContainer);}
waitForAPI(function(){if(!this$1._map){return;}
this$1._initMutant();google.maps.event.addListenerOnce(this$1._mutant,"idle",function(){if(!this$1._map){return;}
this$1._checkZoomLevels();this$1._mutantIsReady=true;});});},onRemove:function(map){L.GridLayer.prototype.onRemove.call(this,map);this._observer.disconnect();map._container.removeChild(this._mutantContainer);if(this._logoContainer){L.DomUtil.remove(this._logoContainer);}
if(this._attributionContainer){L.DomUtil.remove(this._attributionContainer);}
if(this._mutant){google.maps.event.clearListeners(this._mutant,"idle");}},addGoogleLayer:function(googleLayerName,options){var this$1=this;if(!this._subLayers){this._subLayers={};}
this.whenReady(function(){var Constructor=google.maps[googleLayerName];var googleLayer=new Constructor(options);googleLayer.setMap(this$1._mutant);this$1._subLayers[googleLayerName]=googleLayer;});return this;},removeGoogleLayer:function(googleLayerName){var this$1=this;this.whenReady(function(){var googleLayer=this$1._subLayers&&this$1._subLayers[googleLayerName];if(googleLayer){googleLayer.setMap(null);delete this$1._subLayers[googleLayerName];}});return this;},_initMutantContainer:function(){if(!this._mutantContainer){this._mutantContainer=L.DomUtil.create("div","leaflet-google-mutant leaflet-top leaflet-left");this._mutantContainer.id="_MutantContainer_"+L.Util.stamp(this._mutantContainer);this._mutantContainer.style.pointerEvents="none";this._mutantContainer.style.visibility="hidden";L.DomEvent.off(this._mutantContainer);}
this._map.getContainer().appendChild(this._mutantContainer);this.setOpacity(this.options.opacity);var style=this._mutantContainer.style;if(this._map.options.zoomSnap<1){style.width="180%";style.height="180%";}else{style.width="100%";style.height="100%";}
style.zIndex=-1;this._attachObserver(this._mutantContainer);},_initMutant:function(){if(this._mutant){return;}
var map=new google.maps.Map(this._mutantContainer,{center:{lat:0,lng:0},zoom:0,tilt:0,mapTypeId:this.options.type,disableDefaultUI:true,keyboardShortcuts:false,draggable:false,disableDoubleClickZoom:true,scrollwheel:false,styles:this.options.styles||[],backgroundColor:"transparent",});this._mutant=map;this._update();this.fire("spawned",{mapObject:map});this._waitControls();this.once("controls_ready",this._setupAttribution);},_attachObserver:function _attachObserver(node){if(!this._observer){this._observer=new MutationObserver(this._onMutations.bind(this));}
this._observer.observe(node,{childList:true,subtree:true});Array.prototype.forEach.call(node.querySelectorAll("img"),this._boundOnMutatedImage);},_waitControls:function(){var this$1=this;var id=setInterval(function(){var layoutManager=this$1._mutant.__gm.layoutManager;if(!layoutManager){return;}
clearInterval(id);var positions;Object.keys(layoutManager).forEach(function(key){var el=layoutManager[key];if(el.get){if(el.get(1)instanceof Node){positions=el;}}});this$1.fire("controls_ready",{positions:positions});},50);},_setupAttribution:function(ev){var pos=google.maps.ControlPosition;var ctr=(this._attributionContainer=ev.positions.get(pos.BOTTOM_RIGHT));L.DomUtil.addClass(ctr,"leaflet-control leaflet-control-attribution");L.DomEvent.disableClickPropagation(ctr);ctr.style.height="14px";this._map._controlCorners.bottomright.appendChild(ctr);this._logoContainer=ev.positions.get(pos.BOTTOM_LEFT);this._logoContainer.style.pointerEvents="auto";this._map._controlCorners.bottomleft.appendChild(this._logoContainer);},_onMutations:function _onMutations(mutations){for(var i=0;i<mutations.length;++i){var mutation=mutations[i];for(var j=0;j<mutation.addedNodes.length;++j){var node=mutation.addedNodes[j];if(node instanceof HTMLImageElement){this._onMutatedImage(node);}else if(node instanceof HTMLElement){Array.prototype.forEach.call(node.querySelectorAll("img"),this._boundOnMutatedImage);}}}},_roadRegexp:/!1i(\d+)!2i(\d+)!3i(\d+)!/,_satRegexp:/x=(\d+)&y=(\d+)&z=(\d+)/,_staticRegExp:/StaticMapService\.GetMapImage/,_onMutatedImage:function _onMutatedImage(imgNode){var coords;var match=imgNode.src.match(this._roadRegexp);var sublayer=0;if(match){coords={z:match[1],x:match[2],y:match[3],};if(this._imagesPerTile>1){imgNode.style.zIndex=1;sublayer=1;}}else{match=imgNode.src.match(this._satRegexp);if(match){coords={x:match[1],y:match[2],z:match[3],};}
sublayer=0;}
if(coords){var tileKey=this._tileCoordsToKey(coords);imgNode.style.position="absolute";var key=tileKey+"/"+sublayer;this._lru.set(key,imgNode);if(key in this._tileCallbacks&&this._tileCallbacks[key]){this._tileCallbacks[key].forEach(function(callback){return callback(imgNode);});delete this._tileCallbacks[key];}}},createTile:function(coords,done){var key=this._tileCoordsToKey(coords),tileContainer=L.DomUtil.create("div");tileContainer.style.textAlign="left";tileContainer.dataset.pending=this._imagesPerTile;done=done.bind(this,null,tileContainer);for(var i=0;i<this._imagesPerTile;++i){var key2=key+"/"+i,imgNode=this._lru.get(key2);if(imgNode){tileContainer.appendChild(this._clone(imgNode));--tileContainer.dataset.pending;}else{this._tileCallbacks[key2]=this._tileCallbacks[key2]||[];this._tileCallbacks[key2].push(function(c){return function(imgNode){c.appendChild(this._clone(imgNode));--c.dataset.pending;if(!parseInt(c.dataset.pending)){done();}}.bind(this);}.bind(this)(tileContainer));}}
if(!parseInt(tileContainer.dataset.pending)){L.Util.requestAnimFrame(done);}
return tileContainer;},_clone:function(imgNode){var clonedImgNode=imgNode.cloneNode(true);clonedImgNode.style.visibility="visible";return clonedImgNode;},_checkZoomLevels:function(){var zoomLevel=this._map.getZoom(),gMapZoomLevel=this._mutant.getZoom();if(!zoomLevel||!gMapZoomLevel){return;}
if(gMapZoomLevel!==zoomLevel||gMapZoomLevel>this.options.maxNativeZoom){this._setMaxNativeZoom(gMapZoomLevel);}},_setMaxNativeZoom:function(zoomLevel){if(zoomLevel!==this.options.maxNativeZoom){this.options.maxNativeZoom=zoomLevel;this._resetView();}},_update:function(center){if(this._mutant){center=center||this._map.getCenter();var _center=new google.maps.LatLng(center.lat,center.lng),zoom=Math.round(this._map.getZoom()),mutantZoom=this._mutant.getZoom();this._mutant.setCenter(_center);if(zoom!==mutantZoom){this._mutant.setZoom(zoom);if(this._mutantIsReady){this._checkZoomLevels();}}}
L.GridLayer.prototype._update.call(this,center);},whenReady:function(callback,context){if(this._mutant){callback.call(context||this,{target:this});}else{this.on("spawned",callback,context);}
return this;},});L.gridLayer.googleMutant=function(options){return new L.GridLayer.GoogleMutant(options);};})();