var mysql      = require('mysql');
// 비밀번호는 별도의 파일로 분리해서 버전관리에 포함시키지 않아야 합니다. 
var connection = mysql.createConnection({
  host     : 'highlighter-mysql.cpt0ctnfatu9.ap-northeast-2.rds.amazonaws.com',
  user     : 'highlighter',
  password : 'highlighter12',
  database : 'highlighter'
});
connection.connect();
var video_index=2;
//var hpath="\\video2\\hvideo2\\"          
var start = '01:04:01';     
var end='01:05:10';        
//var e1=2;
//var e2=3;
//var e3=4;
connection.query(`SELECT count(*) as c FROM highlightvideo where video_index=?`, 
    [video_index], function (error, results) {      //해당 비디오의 하이라이트영상이 몇개있는지 
    if (error) {
        throw error;
    }
    var hi=(results[0].c)+1;                    //다음 하이라트영상의 인덱스번호
    console.log(hi);
    connection.query(`insert into highlightvideo values(?,?,?,?,?,?,?,?)`,
    [video_index,hi,null,start,end,null,null,null],       //입력받은 값 수정해서 넣으면 됨
    function (error2, results2) {
    if (error2) {
        throw error2;
    }
    connection.end();
    });

});

