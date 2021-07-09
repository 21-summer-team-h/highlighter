var express = require('express');
var app = express();

app.use(express.static('public'));

var sectiondata={
    video_index : 2, 
    start : '01:02:01',    
    end : '01:03:06'   
}

app.post('/api/node/section', function (req, res) {
    res.json(sectiondata);
});
  

app.listen(3010, function () {
  console.log('Server listening on port 3000!');
});