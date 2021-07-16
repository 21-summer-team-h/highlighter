import React, { useEffect, useState } from "react";
import './showResult.css';
import axios from "axios";
import { Row, Col } from 'antd';
import imgFile from "../images/logo1.png";

const ShowResult = () => {
    const [Video, setVideo] = useState([]);

    const emo=["Angry","Disgusting","Fearful", "Happy", "Sad", "Surpring", "Neutral"];   //0~6
    const [Emotion1, setEmotion1] = useState("");
    const [Emotion2, setEmotion2] = useState("");
    const [Emotion3, setEmotion3] = useState("");

    useEffect(()=>{
        axios.get('/api/node/job-end')  //video 편집 완료 메세지
        .then(response => {
            if(response.data.success){ //완료 메세지 수신
                setVideo(response.data.video);
                setEmotion1(emo[response.data.emotion1]);    //0~6사이 숫자 형태로 받아옴
                setEmotion2(emo[response.data.emotion2]);    //0~6사이 숫자 형태로 받아옴
                setEmotion3(emo[response.data.emotion3]);    //0~6사이 숫자 형태로 받아옴
            }else{
                alert("Failed to get Video and Emotion");
            }
        })
    })

    var fileDownload = require('js-file-download');
    const handleDownload = () => {
        axios.get('http://localhost:8000/download', { 
            responseType: 'blob',
        }).then(res => {
            fileDownload(res.data, 'filename.mp4');
            console.log(res);
        }).catch(err => {
            console.log(err);
        })
    }


    return(
        <Row>
            <Col lg={18} xs={24}>
                <div id="mainbox">
                <img id="logo" src={imgFile}/>

                {/* 완성 영상 재생시키기 */}
                <video src={`http://localhost:3000/${Video.video}`} controls></video>

                {/* 다운로드 버튼 구현 */}
                <button class="downloadbutton" onclick={handleDownload}>다운로드</button>

                {/* 태그 보여주기 */}
                <p id="text1">#{Emotion1} #{Emotion2} #{Emotion3}</p>

                </div>
            </Col>            
        </Row>
    )}
    
export default ShowResult;