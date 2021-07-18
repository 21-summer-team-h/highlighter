import React, { useState, useEffect } from "react";
import { Route, Link } from "react-router-dom";
import './sendLink.css';
import axios from "axios";
import ValidateLink from './validateLink';
import Loading from './loading';
import imgFile from '../images/logo1.png';

const SendLink = () => {
    const [videoLink, setVideoLink] = useState("");
    const [linkError, setLinkError] = useState(null);
    const [submitting, setSubmitting] = useState(false);
    const [loading, setLoading] = useState(false);
    const [showButton, setShowButton] = useState(false);

    const handleInputChange = (event) => {
        setVideoLink(event.target.value);
    }

    /* 다운로드 종료 후 실행된다.*/
    const waitForVideo = () => {
        setLoading(true);
        axios.get('/api/edit/')
		    /* 다운로드 종료 후, response 받아 페이지 이동하는 버튼 보여준다. */
            .then(response => {
                setLoading(false);
                alert("Video edited!");
                setShowButton(true);
            })
            .catch(error => {
                alert("Failed to edit video")
            })
    }

    const handleSubmit = (event) => {
        setSubmitting(true);
        event.preventDefault();

        // 유효성을 검사한다.
        let errorMsg = ValidateLink(videoLink);
        if ( errorMsg != ""){
            alert(errorMsg);
        }

        // id만 추출해서 backend로 전송한다.
        else {
            const videoID = videoLink.substring(25,);
            axios.post('/api/download/', { videoID : videoID })
                .then(response => {
                    if (response.data == "Downloaded") {
                        alert("Wait for video!");
                        waitForVideo()
                    }
                    else {
                        alert("Invalid video ID");
                    }
                })
                .catch(error => {
                    alert("Failed to send link.");
                })
        }

        setSubmitting(false);
    }

    return (
        <>
        <div id="mainbox">
            <img id="logo" src={ imgFile }/>
            <p class="text1">Edit highlight moments</p>
            <p class="text1">from twitch</p>
            <br/>
            <form onSubmit={ handleSubmit } id="linkForm">
                <input
                    type="text"
                    id="linkInputBox"
                    placeholder="Twitch Link"
                    onChange={ handleInputChange }>
                </input>
                <button type="submit" id="submitButton" submitting="submitting">Edit</button>
            </form>
            <div id="progressStatus">{loading? <Loading/> : ""}</div>
            {/* 작업 종료 후, page 4로 이동할 수 있는 버튼을 보여준다. */}
            {showButton ? <Link to="/result" id="getVideoButton">Get video</Link> : ""}
        </div>
        </>
    )
}

export default SendLink;