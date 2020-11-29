var streamMap = L.map('mapid').setView([43.6629, -79.3957], 16);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 20,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYW5oYXNzYW4iLCJhIjoiY2tpMHRlcGp2MTBidTJycXE4bTFxNjUxZiJ9.a4A1JGv7W5zgk0pHKMADxw'
}).addTo(streamMap);

var bus1Icon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
    iconSize:     [30, 40]
});

var bus2Icon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    iconSize:     [30, 40]
});

var bus3Icon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    iconSize:     [30, 40]
});


markerList1 = [];
markerList2 = [];
markerList3 = [];
var index = 0; 
busIds = ["0001","0002","0003"];

var source = new EventSource("/topic");

source.onmessage = function(stream){
    console.log(stream);
    var streamObject = JSON.parse(stream.data);
    var streamBusCode = streamObject["key"].substr(0,4);
    if(streamBusCode == busIds[0]){
        if(markerList1.length !=0){
            streamMap.removeLayer(markerList1[0]);
            markerList1.pop();
        }
        var busMarker1 = new L.marker([streamObject["latitude"],streamObject['longitude']],{icon: bus1Icon});
        markerList1.push(busMarker1);
        streamMap.addLayer(busMarker1);
    }

    if(streamBusCode == busIds[1]){
        if(markerList2.length != 0 ){
            streamMap.removeLayer(markerList2[0]);
            markerList2.pop();
        }
        var busMarker2 = new L.marker([streamObject["latitude"],streamObject["longitude"]],{icon: bus2Icon});
        markerList2.push(busMarker2);
        streamMap.addLayer(busMarker2);
    }

    if(streamBusCode == busIds[2]){
        if(markerList3.length != 0 ){
            streamMap.removeLayer(markerList3[0]);
            markerList3.pop();
        }
        var busMarker3 = new L.marker([streamObject["latitude"],streamObject["longitude"]],{icon: bus3Icon});
        markerList3.push(busMarker3);
        streamMap.addLayer(busMarker3);
    }
}
