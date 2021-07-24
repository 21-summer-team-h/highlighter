import React, { useState, useEffect } from "react";
import { Route, Link } from "react-router-dom";
import './sendLink.css';
import axios from "axios";
import ValidateLink from './validateLink';
import Loading from './loading';
import logoImg from '../images/logo.png';
import folderImg from '../images/folder.png';

const SendLink = () => {
    const [videoLink, setVideoLink] = useState("");
    const [linkError, setLinkError] = useState(null);
    const [submitting, setSubmitting] = useState(false);
    const [loading, setLoading] = useState(false);
    const [showButton, setShowButton] = useState(false);
    const [showGo, setShowGo] = useState(true);
    const [videoIndex, setVideoIndex] = useState();

    const handleInputChange = (event) => {
        setVideoLink(event.target.value);
    }

    const handleSubmit = (event) => {
        setSubmitting(true);
        setLoading(true);
        setShowGo(false);
        event.preventDefault();

        // 유효성을 검사한다.
        let errorMsg = ValidateLink(videoLink);
        if ( errorMsg != ""){
            setLoading(false);
            setShowGo(true);
            alert(errorMsg);
        }

        // id만 추출해서 backend로 전송한다.
        else {
            const videoID = videoLink.substring(29,);
            console.log(videoID);
            axios.post('/api/download/', { videoID : videoID })
                .then(response => {
                    if (response.data == "No video") {
                        setLoading(false);
                        setShowGo(true);
                        alert("Fail");
                    }
                    else {
                        alert("Wait for video!");
                        setVideoIndex(response.data);
                        setLoading(false);
                        setShowButton(true);
                    }
                })
                .catch(error => {
                    setLoading(false);
                    setShowGo(true);
                    alert("Failed to send link.");
                })
        }

        setSubmitting(false);
    }

    return (
        <>
        <div id="mainbox">
            <hr id="line1"></hr>
            <hr id="line2"></hr>
            <img id="logo" src={ logoImg }/>
            <div class="leftbar">
                <div class="folder"><img id = "folderImg" src={ folderImg }/><span>Uploads</span></div>
                <div class="folder"><img id = "folderImg" src={ folderImg }/><span>Broadcast</span></div>
                <div class="folder"><img id = "folderImg" src={ folderImg }/><span>Shares</span></div>
                <div class="folder"><img id = "folderImg" src={ folderImg }/><span>Highlighter</span></div>
                <div class="folder" id="open"><img id = "folderImg" src={ folderImg }/><span>Edit</span></div>
            </div>
            <p id="text">Get 10-minute highlights from twitch</p>
            <form onSubmit={ handleSubmit } id="linkForm">
                <input
                    type="text"
                    id="linkInputBox"
                    placeholder="Twitch Link"
                    onChange={ handleInputChange }>
                </input>
                {showGo ? <button type="submit" id="submitButton" class="btn" submitting="submitting">GO</button> : ""}
            </form>
            <div id="progressStatus">{loading? <Loading/> : ""}</div>
            {/* 작업 종료 후, page 4로 이동할 수 있는 버튼을 보여준다. */}
            {showButton ?
                <Link to= {{
                    pathname: "/result",
                    state: { videoIndex : videoIndex }
                }}
                style={{ textDecoration: 'none' }}>
                <button class="btn" id="getVideoButton" >Get video</button>
                </Link> 
                : ""
            }
        </div>
        </>
    )
}

export default SendLink;