import React, { useEffect, useState } from "react";
import { Route, Link } from "react-router-dom";
import './showResult.css';
import axios from "axios";
import logoImg from "../images/logo.png";


const ShowResult = (props) => {
    const [Video, setVideo] = useState([]);
    const [videoIndex, setVideoIndex] = useState(null);

    // setVideoIndex(props.location.state.videoIndex);
    // console.log(videoIndex);

    const emo=["Angry","Disgusting","Fearful", "Happy", "Sad", "Surpring", "Neutral"];   //0~6
    const [Emotion1, setEmotion1] = useState();
    const [Emotion2, setEmotion2] = useState();
    const [Emotion3, setEmotion3] = useState();
    const [Emotion4, setEmotion4] = useState();
    const [Emotion5, setEmotion5] = useState();

    useEffect(()=>{
        axios.get('/api/node/job-end') //video 편집 완료 메세지
        .then(response => {          
                setVideo(response.data.video);                      
        })
        .catch(error =>{
            console.log(error)
        })

        axios.get('/api/getEmotion/')   //backend에게 emotion요청
        .then(response => {
            setEmotion1(emo[response.data.emotion1]);    //0~6사이 숫자 형태로 받아옴
            setEmotion2(emo[response.data.emotion2]);    
            setEmotion3(emo[response.data.emotion3]);   
            setEmotion4(emo[response.data.emotion4]);    
            setEmotion5(emo[response.data.emotion5]);        
        })
        .catch(error=>{
            console.log(error)
        })
    })

    var fileDownload = require('js-file-download');

    const handleDownload = () => {
        axios.get("/api/getVideo/{videoIndex}",{
            responseType:'blob'
        }).then(res => {
            fileDownload(res.data,'filename.mp4')
            console.log(res)
        }).catch(error=>{
            console.log(error)
        })
    }


    return (
        <>
        <div id="mainbox">
            <hr id="line1"></hr>
            <hr id="line2"></hr>
            <img id="logo" src={logoImg}/>

            {/* 완성 영상 재생시키기
            <video id="show_video" width="2600" height="2000" src={}} controls></video>
            controls이 존재하면, 소리 조절(volume), 동영상 탐색(seek), 일시 정지(pause)/재시작(resume)을 할 수 있는 컨트롤러를 제공합니다.*/}

            <div id="videoBox"></div>
            {/* 다운로드 버튼 구현 */}
            <button id="downloadButton" class="btn" /* onclick={ handleDownload } */ >Download</button>

            {/* 태그 보여주기 */}
            <p id="tag">#{Emotion1} #{Emotion2} #{Emotion3} #{Emotion4} #{Emotion5}</p> 

        </div>
        </>
    )
}
    
export default ShowResult;