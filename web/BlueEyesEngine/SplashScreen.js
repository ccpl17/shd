/*****************************************************/
/*                  BlueEyes Engine                  */
/*                  Splash Screen                    */
/*                                                   */
/* Version 1.0.10                                    */
/* Date 2022/12/21                                   */
/* Coded by Cenlun Chung Po Lun                      */
/*****************************************************/

const SplashScreen = document.querySelector(".SplashScreen");

document.addEventListener("DOMContentLoaded", (e)=>{
    setTimeout(()=>{
        SplashScreen.classList.add("display-none");
    }, 1000);
    setTimeout(()=>{
        document.location.href = "Home.html";
    }, 1750);
});