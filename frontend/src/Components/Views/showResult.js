import React, { useEffect, useState } from "react";
import './showResult.css';
import axios from "axios";
import logoImg from "../images/logo.png";
import Facebook_logo from "../images/facebook-logo.png";
import Youtube_logo from "../images/youtube-logo.png";
import Twitter_logo from "../images/twitter-logo.png";
import Instagram_logo from "../images/instagram-logo.png";


const ShowResult = (props) => {
    const [Video, setVideo] = useState([]);
    const videoIndex = props.location.state.videoIndex;

    const emo=["Angry","Disgusting","Fearful", "Happy", "Sad", "Surpring", "Neutral"];   //0~6
    const [Emotion1, setEmotion1] = useState();
    const [Emotion2, setEmotion2] = useState();
    const [Emotion3, setEmotion3] = useState();
    const [Emotion4, setEmotion4] = useState();
    const [Emotion5, setEmotion5] = useState();

    
    useEffect(()=>{
        axios.post('/api/getEmotion/', {
            video_index : videoIndex
        })   //backend에게 emotion요청
        .then(response => {
            let emotion_list = response.data.emotion_list;
            setEmotion1(emo[emotion_list[0]]);    //0~6사이 숫자 형태로 받아옴
            setEmotion2(emo[emotion_list[1]]);    
            setEmotion3(emo[emotion_list[2]]);   
            setEmotion4(emo[emotion_list[3]]);    
            setEmotion5(emo[emotion_list[4]]);        
        })
        .catch(error=>{
            console.log(error)
        }, [])
    })

    var fileDownload = require('js-file-download');

    const handleDownload = (e) => {
        e.preventDefault();

        axios.get("/api/getVideo/",{
            params: {
                video_index: videoIndex,
            },
            responseType:'blob'
        }).then(res => {
            fileDownload(res.data,'highlight.mp4')
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
            <div class="leftbar">
                <div class="folder"><span>Upload & Share</span></div>
                <br></br>
                <div><img id = "snsLogoImg" src={ Facebook_logo }/><a class="goSns" target="_blank" href="https://facebook.com">Facebook</a><span></span></div>
                <br></br>
                <div><img id = "snsLogoImg" src={ Twitter_logo }/><a class="goSns" target="_blank" href="https://twitter.com">Twitter</a><span></span></div>
                <br></br>
                <div><img id = "snsLogoImg" src={ Instagram_logo }/><a class="goSns" target="_blank" href="https://instagram.com">Instagram</a><span></span></div>
                <br></br>
                <div><img id = "snsLogoImg" src={ Youtube_logo }/><a class="goSns" target="_blank" href="https://youtube.com">Youtube</a><span></span></div>
            </div>
            {/* 완성 영상 재생시키기
            <video id="show_video" width="2600" height="2000" src={}} controls></video>
            controls이 존재하면, 소리 조절(volume), 동영상 탐색(seek), 일시 정지(pause)/재시작(resume)을 할 수 있는 컨트롤러를 제공합니다.*/}

            <div id="videoBox"></div>
            {/* 다운로드 버튼 구현 */}

            <form onSubmit = { handleDownload }>
                <button type="submit" id="downloadButton" class="btn">Download</button>
            </form>

            {/* 태그 보여주기 */}
            <p id="tag">#{Emotion1} #{Emotion2} #{Emotion3} #{Emotion4} #{Emotion5}</p> 

        </div>
        </>
    )
}
    
export default ShowResult;