var loginWidgetLoadFailure = false;
var ghpBannerloginLoadFail = false;

function isMobile() {
    const minWidth = 1056; // Minimum width for desktop devices
    return window.innerWidth < minWidth || screen.width < minWidth;
}
document.addEventListener('DOMContentLoaded', function () {
    if (!isMobile()) {
       
    setTimeout(function () {
            if (document.querySelector('.ghpBanner')) {
                try {
                    var loginWidget = document.querySelector(' #ReactLoginWidgetApp');
                    if (!loginWidget) {
                        var fallbackText = document.querySelector('.fallback-text');
                        fallbackText.classList.remove('is-hidden');
                        fallbackText.classList.add('is-fallBack');
                        var authLoginRwc = document.querySelectorAll('auth-login-rwc[redirect="true"]');
                        if (authLoginRwc) {
                            authLoginRwc.forEach(e => e.remove());
                        }
                        ghpBannerloginLoadFail = true;
                        throw new Error('Sorry login widget fail to load in Ghp Banner' + new Date().toUTCString());
                    }else{
                        document.querySelectorAll('.skeleton').forEach(e => e.remove());
                    }
                } catch (error) {
                    console.error('An error occurred:', error);
                }

            }

        }, 5000);
    }
});

function myDisplayer(some) {
    if (some) {
        return;
    }
  }

  async function skeletonLoader() {
    const intervalId = setInterval(() => {
      const element = document.querySelector(' #ReactLoginWidgetApp');
      const fallbackText = document.querySelector('.fallback-text.is-fallBack');
      if (element || fallbackText) {
        clearInterval(intervalId);
        var skeleton = document.querySelectorAll('.skeleton');
        var loginWidgetSkeleton = document.querySelector('.loginWidgetSkeleton');
        loginWidgetSkeleton.remove();
        skeleton.forEach(e => e.remove());
        return true;
      }
    }, 100); // Check every 100 milliseconds

  }

  skeletonLoader().then(
    function (value) { myDisplayer(value); },
    function (error) { myDisplayer(error); }
  );


    const mediaQuery = window.matchMedia('(min-width: 1056px)');
    // Function to run when the breakpoint is crossed
    function handleViewportChange(e) {
        if (e.matches) {
            // Viewport is now desktop size
            console.log('Switched to desktop view');
            let uat = /(uat3|uat5|it02|it5|it03|stage)/gi.test(window.location.href) == true;
            let authURL ="https://uat3-onlinebanking.usbank.com/auth/login/rwc/main-bundle.js";
            if(!uat) {
                authURL ="https://onlinebanking.usbank.com/auth/login/rwc/main-bundle.js";
            }
            let len = document.querySelectorAll('script[src="' + authURL + '"]').length;
            if(len > 0) {
                console.log("Script already loaded");
                return;
            }else{            
                let onlinbankingUrl = authURL;
                let scriptTag = document.createElement('script');
                scriptTag.src = onlinbankingUrl;
                document.head.appendChild(scriptTag);
            }
        } else {
        // Viewport is now mobile size
            console.log("Switched to mobile view so don't load script");
         }
        }
            document.addEventListener('DOMContentLoaded', function () {
            // Initial check
            handleViewportChange(mediaQuery);
            // Listen for changes
            mediaQuery.addEventListener('change', handleViewportChange);
            });
