export default function ValidateLink(link) {
    let error = "";

    if (link == "") {
      error = "No link";

    } else {
        let Url = /https:\/\/www.twitch.tv\/videos\/[0-9].{3,20}/;
        let urlTest = Url.test(link);

        if(!urlTest){
          error = "Not a twitch video url";
        }
    }
  
    return error;
  }