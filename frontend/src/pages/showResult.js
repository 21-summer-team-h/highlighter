import React, { useEffect, useState } from "react";
import { Route, Link, useHistory, useLocation } from "react-router-dom";
import './showResult.css';
import axios from "axios";
import Loading from './components/loading';
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
    const [loader, setLoader] = useState(true);
    const [showB, setShowB] = useState(false);
    const [thumb, setThumb] = useState(0);

    const emotionTags = checkedEmo.map((e, index) => (<li key={index}>#{EMOTIONS[e]}</li>));

    const [Video, setVideo] = useState([]);
    var fileDownload = require('js-file-download');

    useEffect(() => {
        axios.get("/api/getMainImg/", { 
            params: { 
                video_index: videoIndex, 
            }
        })
        .then(response => {
            if (response.data == {}){
                alert("Failed to show thumbnail");
            }
            else {
                setLoader(false);
                let thumbnail = response.data;
                setThumb(thumbnail);
                setShowB(true);
            }
        })
        .catch(error => {
            console.log(error)
        })
    }, [])

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
                <div><img id = "snsLogoImg" src={ Facebook_logo }/><a class="goSns" target="_blank" href="https://facebook.com">Facebook</a></div> 
                <br></br> 
                <div><img id = "snsLogoImg" src={ Twitter_logo }/><a class="goSns" target="_blank" href="https://twitter.com">Twitter</a></div> 
                <br></br> 
                <div><img id = "snsLogoImg" src={ Instagram_logo }/><a class="goSns" target="_blank" href="https://instagram.com">Instagram</a></div> 
                <br></br> 
                <div><img id = "snsLogoImg" src={ Youtube_logo }/><a class="goSns" target="_blank" href="https://youtube.com">Youtube</a></div> 
            </div> 

            {/* ?????? ?????? ???????????????
            <video id="show_video" width="2600" height="2000" src={}} controls></video>
            controls??? ????????????, ?????? ??????(volume), ????????? ??????(seek), ?????? ??????(pause)/?????????(resume)??? ??? ??? ?????? ??????????????? ???????????????.*/}

            <div id="videoBox">
                {thumb ? <img id="thumbnail" src={"data:image/png;base64,"+ thumb }></img> : ""}
            </div>

            <div class="emotionTags">
                { emotionTags }
            </div>

            <div id="loader">{loader ? <Loading/> : ""}</div>

            <form onSubmit = { handleDownload }>
                <button type="submit" id="downloadButton" class="btn"
                style = {showB ? { visibility : "visible" } : { visibility: "hidden" }}>
                Download</button>
            </form>

        </div>
        </>
    )
}
    
export default ShowResult;