import React, { useEffect, useState } from "react";
import { Route, Link, useHistory, useLocation } from "react-router-dom";
import './showResult.css';
import axios from "axios";
import logoImg from "./images/logo.png";
import Facebook_logo from "./images/facebook-logo.png"; 
import Youtube_logo from "./images/youtube-logo.png"; 
import Twitter_logo from "./images/twitter-logo.png"; 
import Instagram_logo from "./images/instagram-logo.png";

const EMOTIONS = ["Angry","Disgusting","Fearful", "Happy", "Sad", "Surpring", "Neutral"];   //0~6

// page 3
const ShowResult = (props) => {
    const location = useLocation();
    const videoIndex = location.state.videoIndex;
    const checkedEmo = location.state.checkedEmo;

    const emotionTags = checkedEmo.map((e, index) => (<li key={index}>#{EMOTIONS[e]}</li>));

    const [Video, setVideo] = useState([]);
    const [thumbnail, setThumbnail] = useState([]);
    var fileDownload = require('js-file-download');

    useEffect(() => {
        axios.get("/api/getMainImg/",{ 
            params: { 
                video_index: videoIndex,
            }
        })
        .then(response => {
            if (response.data == {}){
                alert("Failed to show clips");
            }
            else {
                // console.log("thumbnail data : " + String(response.data)).substring(0, 10);
                // console.log("thumbnail data : " + JSON.stringify(response.data.thumbnail).substring(0, 10));
                // setThumbnail(String(response.data));
                setThumbnail('//localhost/usr/src/app/videos/vo' + videoIndex + '.png')
            }
        })
        .catch(error => {
            console.log(error)
        })
    }, [])

    const handleDownload = (e) => {
        e.preventDefault();
        console.log("download");

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
                <div><img id = "snsLogoImg" src={ Facebook_logo }/><a class="goSns" target="_blank" href="https://facebook.com">Facebook</a></div> 
                <br></br> 
                <div><img id = "snsLogoImg" src={ Twitter_logo }/><a class="goSns" target="_blank" href="https://twitter.com">Twitter</a></div> 
                <br></br> 
                <div><img id = "snsLogoImg" src={ Instagram_logo }/><a class="goSns" target="_blank" href="https://instagram.com">Instagram</a></div> 
                <br></br> 
                <div><img id = "snsLogoImg" src={ Youtube_logo }/><a class="goSns" target="_blank" href="https://youtube.com">Youtube</a></div> 
            </div> 

            {/* 완성 영상 재생시키기
            <video id="show_video" width="2600" height="2000" src={}} controls></video>
            controls이 존재하면, 소리 조절(volume), 동영상 탐색(seek), 일시 정지(pause)/재시작(resume)을 할 수 있는 컨트롤러를 제공합니다.*/}

            <div id="videoBox">
                
                <img src={"data:image/png;base64,"+ thumbnail }></img>
            </div>

            <div class="emotionTags">
                { emotionTags }
            </div>

            <form onSubmit = { handleDownload }>
                <button type="submit" id="downloadButton" class="btn">Download</button>
            </form>

        </div>
        </>
    )
}
    
export default ShowResult;