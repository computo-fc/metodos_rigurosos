


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>metodos_rigurosos/clases/intervalo.py at master · ljml27/metodos_rigurosos</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="github-fe120-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 1.9.3p194-tcs-github-tcmalloc (2012-05-25, TCS patched 2012-05-27, GitHub v1.0.36) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="xhr-socket" href="/_sockets" />
    
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="C98DC6717E921EF4DD95234F1CF" name="octolytics-dimension-request_id" /><meta content="5274173" name="octolytics-actor-id" /><meta content="ljml27" name="octolytics-actor-login" /><meta content="a2ea260b55f313eaaba21b438a671933428a69b59253041d4fa09b5b6550ae6c" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="JcX42+5bWLzuJ5gfSzuSMCXZ0nQ3QgrCmkU1W4XLGDg=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-1e4633e47f8b05996d0513eaccf94c2ff0a6a243.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-a7192edf5255443a92680441f722274ed90a93eb.css" media="all" rel="stylesheet" type="text/css" />
    

    

      <script src="https://github.global.ssl.fastly.net/assets/frameworks-f86a2975a82dceee28e5afe598d1ebbfd7109d79.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-15065af1aa90bd5052d5662dc59db098b822916e.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="150dbead5d79b419ec8e5c73a14151c0">

        <link data-pjax-transient rel='permalink' href='/ljml27/metodos_rigurosos/blob/34c9e91136e470f0b3525df553f87985ca02e178/clases/intervalo.py'>
  <meta property="og:title" content="metodos_rigurosos"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/ljml27/metodos_rigurosos"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="metodos_rigurosos - Materiales del curso de Métodos Numéricos Rigurosos"/>

  <meta name="description" content="metodos_rigurosos - Materiales del curso de Métodos Numéricos Rigurosos" />

  <meta content="5274173" name="octolytics-dimension-user_id" /><meta content="ljml27" name="octolytics-dimension-user_login" /><meta content="12581285" name="octolytics-dimension-repository_id" /><meta content="ljml27/metodos_rigurosos" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="12110981" name="octolytics-dimension-repository_parent_id" /><meta content="computo-fc/metodos_rigurosos" name="octolytics-dimension-repository_parent_nwo" /><meta content="12110981" name="octolytics-dimension-repository_network_root_id" /><meta content="computo-fc/metodos_rigurosos" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/ljml27/metodos_rigurosos/commits/master.atom" rel="alternate" title="Recent Commits to metodos_rigurosos:master" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production windows vis-public fork page-blob">
    <div class="wrapper">
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    <div class="divider-vertical"></div>

    
    <a href="/notifications" class="notification-indicator tooltipped downwards" data-gotokey="n" title="You have unread notifications">
        <span class="mail-status unread"></span>
</a>    <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey=" s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="ljml27"
      data-repo="ljml27/metodos_rigurosos"
      data-branch="master"
      data-sha="1407392415666236ab897bdf3699d4efec892144"
  >

    <input type="hidden" name="nwo" value="ljml27/metodos_rigurosos" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    


  <ul id="user-links">
    <li>
      <a href="/ljml27" class="name">
        <img height="20" src="https://2.gravatar.com/avatar/f8041ec27ffeeabd3331254608728181?d=https%3A%2F%2Fidenticons.github.com%2Fc6c8b3949fdd40e2c96cedf70fd49d37.png&amp;s=140" width="20" /> ljml27
      </a>
    </li>

      <li>
        <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo" aria-label="Create a new repo">
          <span class="octicon octicon-repo-create"></span>
        </a>
      </li>

      <li>
        <a href="/settings/profile" id="account_settings"
          class="tooltipped downwards"
          aria-label="Account settings "
          title="Account settings ">
          <span class="octicon octicon-tools"></span>
        </a>
      </li>
      <li>
        <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out" aria-label="Sign out">
          <span class="octicon octicon-log-out"></span>
        </a>
      </li>

  </ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="ljml27/metodos_rigurosos">This repository</span>
    </li>
    <li>
      <a href="/ljml27/metodos_rigurosos/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
      <li>
        <a href="/ljml27/metodos_rigurosos/settings/collaboration"><span class="octicon octicon-person-add"></span> New collaborator</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

      




          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="JcX42+5bWLzuJ5gfSzuSMCXZ0nQ3QgrCmkU1W4XLGDg=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="12581285" />

    <div class="select-menu js-menu-container js-select-menu">
        <a class="social-count js-social-count" href="/ljml27/metodos_rigurosos/watchers">
          1
        </a>
      <span class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0">
        <span class="js-select-button">
          <span class="octicon octicon-eye-unwatch"></span>
          Unwatch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  
<div class="js-toggler-container js-social-container starring-container ">
  <a href="/ljml27/metodos_rigurosos/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
  </a>
  <a href="/ljml27/metodos_rigurosos/star" class="minibutton with-count js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star"></span><span class="text">Star</span>
  </a>
  <a class="social-count js-social-count" href="/ljml27/metodos_rigurosos/stargazers">0</a>
</div>

  </li>


        <li>
          <a href="/ljml27/metodos_rigurosos/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="nofollow" data-method="post">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/ljml27/metodos_rigurosos/network" class="social-count">20</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo-forked"></span>
          <span class="author">
            <a href="/ljml27" class="url fn" itemprop="url" rel="author"><span itemprop="title">ljml27</span></a></span
          ><span class="repohead-name-divider">/</span><strong
          ><a href="/ljml27/metodos_rigurosos" class="js-current-repository js-repo-home-link">metodos_rigurosos</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

            <span class="fork-flag">
              <span class="text">forked from <a href="/computo-fc/metodos_rigurosos">computo-fc/metodos_rigurosos</a></span>
            </span>
        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container ">

        <div class="repository-sidebar">
            

<div class="repo-nav repo-nav-full js-repository-container-pjax js-octicon-loaders">
  <div class="repo-nav-contents">
    <ul class="repo-menu">
      <li class="tooltipped leftwards" title="Code">
        <a href="/ljml27/metodos_rigurosos" aria-label="Code" class="js-selected-navigation-item selected" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /ljml27/metodos_rigurosos">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


      <li class="tooltipped leftwards" title="Pull Requests"><a href="/ljml27/metodos_rigurosos/pulls" aria-label="Pull Requests" class="js-selected-navigation-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /ljml27/metodos_rigurosos/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped leftwards" title="Wiki">
          <a href="/ljml27/metodos_rigurosos/wiki" aria-label="Wiki" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_wiki /ljml27/metodos_rigurosos/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="repo-menu-separator"></div>
    <ul class="repo-menu">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/ljml27/metodos_rigurosos/pulse" aria-label="Pulse" class="js-selected-navigation-item " data-pjax="true" data-selected-links="pulse /ljml27/metodos_rigurosos/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/ljml27/metodos_rigurosos/graphs" aria-label="Graphs" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_graphs repo_contributors /ljml27/metodos_rigurosos/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/ljml27/metodos_rigurosos/network" aria-label="Network" class="js-selected-navigation-item js-disable-pjax" data-selected-links="repo_network /ljml27/metodos_rigurosos/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


      <div class="repo-menu-separator"></div>
      <ul class="repo-menu">
        <li class="tooltipped leftwards" title="Settings">
          <a href="/ljml27/metodos_rigurosos/settings" data-pjax aria-label="Settings">
            <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </a>
        </li>
      </ul>
  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/ljml27/metodos_rigurosos.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/ljml27/metodos_rigurosos.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:ljml27/metodos_rigurosos.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:ljml27/metodos_rigurosos.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/ljml27/metodos_rigurosos" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/ljml27/metodos_rigurosos" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>


  <a href="github-windows://openRepo/https://github.com/ljml27/metodos_rigurosos" class="minibutton sidebar-button">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/ljml27/metodos_rigurosos/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:4ea5eaa1f2c4c5a61e9bf76c409dfbcb -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:4ea5eaa1f2c4c5a61e9bf76c409dfbcb -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/ljml27/metodos_rigurosos/find/master" data-pjax data-hotkey="t" style="display:none">Show File Finder</a>

<div class="file-navigation">
  


<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/ljml27/metodos_rigurosos/blob/implementaciones/clases/intervalo.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="implementaciones" data-skip-pjax="true" rel="nofollow" title="implementaciones">implementaciones</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/ljml27/metodos_rigurosos/blob/master/clases/intervalo.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" data-skip-pjax="true" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/ljml27/metodos_rigurosos/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="JcX42+5bWLzuJ5gfSzuSMCXZ0nQ3QgrCmkU1W4XLGDg=" /></div>
            <span class="octicon octicon-git-branch-create select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master" />
            <input type="hidden" name="path" id="branch" value="clases/intervalo.py" />
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ljml27/metodos_rigurosos" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">metodos_rigurosos</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ljml27/metodos_rigurosos/tree/master/clases" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">clases</span></a></span><span class="separator"> / </span><strong class="final-path">intervalo.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="clases/intervalo.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://0.gravatar.com/avatar/0fb5c31cf152d2f69b47487a377aa59d?d=https%3A%2F%2Fidenticons.github.com%2Fc1df2843b1629b4993f0f02977df2db1.png&amp;s=140" width="24" />
    <span class="author"><a href="/dinomordelon" rel="author">dinomordelon</a></span>
    <time class="js-relative-date" datetime="2013-09-11T08:32:55-07:00" title="2013-09-11 08:32:55">September 11, 2013</time>
    <div class="commit-title">
        <a href="/ljml27/metodos_rigurosos/commit/e0f392307b21a0eed7cbbc9c4afd9dade834efec" class="message" data-pjax="true" title="Se arregló el error de la función reciprocal() para intervalos que conti...

...enen el cero, también se hizo un pequeño cambio en el return de la función de división para llamar a la función reciprocal">Se arregló el error de la función reciprocal() para intervalos que co…</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>9</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="dinomordelon" href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py?author=dinomordelon"><img height="20" src="https://0.gravatar.com/avatar/0fb5c31cf152d2f69b47487a377aa59d?d=https%3A%2F%2Fidenticons.github.com%2Fc1df2843b1629b4993f0f02977df2db1.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="lbenet" href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py?author=lbenet"><img height="20" src="https://1.gravatar.com/avatar/7c0004bc6ff941f7adbd05f3b799bdeb?d=https%3A%2F%2Fidenticons.github.com%2F72140990530ec5fde982d70813383f87.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="computo-fc" href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py?author=computo-fc"><img height="20" src="https://1.gravatar.com/avatar/9ba139ccdb48967958efd0cda23e5d29?d=https%3A%2F%2Fidenticons.github.com%2F56e1d71c2a53ef9ece0b96e3dee7b27c.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="miguelmaya" href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py?author=miguelmaya"><img height="20" src="https://0.gravatar.com/avatar/f8548513e7c14ecd18ff6a1161f4b9dd?d=https%3A%2F%2Fidenticons.github.com%2Ff29d5428876e9324672a82d4aa776a90.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="dpsanders" href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py?author=dpsanders"><img height="20" src="https://0.gravatar.com/avatar/7973472a5ff79302e45e3de5e385bec6?d=https%3A%2F%2Fidenticons.github.com%2F0d4d69a8ae200d95adac30bc05906b5d.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="lorenaphys" href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py?author=lorenaphys"><img height="20" src="https://1.gravatar.com/avatar/7ff82dc8149edc2afaf4e45e41ee0e42?d=https%3A%2F%2Fidenticons.github.com%2Fdc63e1ef1461004ee27baf699c464906.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="davidphysdavalos" href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py?author=davidphysdavalos"><img height="20" src="https://0.gravatar.com/avatar/ef4c0bba02b93a762d74eeac5ea40808?d=https%3A%2F%2Fidenticons.github.com%2F706fbf6fa94a92d6a1b64496eefd5960.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="andresastorga" href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py?author=andresastorga"><img height="20" src="https://2.gravatar.com/avatar/37a5004519a872c9f6d0eff4b4c7257e?d=https%3A%2F%2Fidenticons.github.com%2Fc061364fa07a523e54f160d83ce45e68.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="AsTLAN" href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py?author=AsTLAN"><img height="20" src="https://1.gravatar.com/avatar/73239f00c6c2902e8a2bc656cc3e58ab?d=https%3A%2F%2Fidenticons.github.com%2F3e0153c6ef51447f37aad83514a2fac4.png&amp;s=140" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li class="facebox-user-list-item">
          <img height="24" src="https://0.gravatar.com/avatar/0fb5c31cf152d2f69b47487a377aa59d?d=https%3A%2F%2Fidenticons.github.com%2Fc1df2843b1629b4993f0f02977df2db1.png&amp;s=140" width="24" />
          <a href="/dinomordelon">dinomordelon</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://1.gravatar.com/avatar/7c0004bc6ff941f7adbd05f3b799bdeb?d=https%3A%2F%2Fidenticons.github.com%2F72140990530ec5fde982d70813383f87.png&amp;s=140" width="24" />
          <a href="/lbenet">lbenet</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://1.gravatar.com/avatar/9ba139ccdb48967958efd0cda23e5d29?d=https%3A%2F%2Fidenticons.github.com%2F56e1d71c2a53ef9ece0b96e3dee7b27c.png&amp;s=140" width="24" />
          <a href="/computo-fc">computo-fc</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://0.gravatar.com/avatar/f8548513e7c14ecd18ff6a1161f4b9dd?d=https%3A%2F%2Fidenticons.github.com%2Ff29d5428876e9324672a82d4aa776a90.png&amp;s=140" width="24" />
          <a href="/miguelmaya">miguelmaya</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://0.gravatar.com/avatar/7973472a5ff79302e45e3de5e385bec6?d=https%3A%2F%2Fidenticons.github.com%2F0d4d69a8ae200d95adac30bc05906b5d.png&amp;s=140" width="24" />
          <a href="/dpsanders">dpsanders</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://1.gravatar.com/avatar/7ff82dc8149edc2afaf4e45e41ee0e42?d=https%3A%2F%2Fidenticons.github.com%2Fdc63e1ef1461004ee27baf699c464906.png&amp;s=140" width="24" />
          <a href="/lorenaphys">lorenaphys</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://0.gravatar.com/avatar/ef4c0bba02b93a762d74eeac5ea40808?d=https%3A%2F%2Fidenticons.github.com%2F706fbf6fa94a92d6a1b64496eefd5960.png&amp;s=140" width="24" />
          <a href="/davidphysdavalos">davidphysdavalos</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://2.gravatar.com/avatar/37a5004519a872c9f6d0eff4b4c7257e?d=https%3A%2F%2Fidenticons.github.com%2Fc061364fa07a523e54f160d83ce45e68.png&amp;s=140" width="24" />
          <a href="/andresastorga">andresastorga</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://1.gravatar.com/avatar/73239f00c6c2902e8a2bc656cc3e58ab?d=https%3A%2F%2Fidenticons.github.com%2F3e0153c6ef51447f37aad83514a2fac4.png&amp;s=140" width="24" />
          <a href="/AsTLAN">AsTLAN</a>
        </li>
      </ul>
    </div>
  </div>


<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>220 lines (172 sloc)</span>
        <span>6.634 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
                <a class="minibutton"
                   href="/ljml27/metodos_rigurosos/edit/master/clases/intervalo.py"
                   data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
          <a href="/ljml27/metodos_rigurosos/raw/master/clases/intervalo.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/ljml27/metodos_rigurosos/blame/master/clases/intervalo.py" class="button minibutton ">Blame</a>
          <a href="/ljml27/metodos_rigurosos/commits/master/clases/intervalo.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
            <a class="minibutton danger empty-icon tooltipped downwards"
               href="/ljml27/metodos_rigurosos/delete/master/clases/intervalo.py"
               title=""
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
            Delete
          </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>

            </td>
            <td class="blob-line-code">
                    <div class="highlight"><pre><div class='line' id='LC1'><br/></div><div class='line' id='LC2'><span class="c"># -*- coding: utf-8 -*- </span></div><div class='line' id='LC3'><br/></div><div class='line' id='LC4'><span class="k">class</span> <span class="nc">Intervalo</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC5'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC6'><span class="sd">    Se define la clase &#39;Intervalo&#39;, y los métodos para la aritmética básica de intervalos,</span></div><div class='line' id='LC7'><span class="sd">    es decir, suma, resta, multiplicación y división. Se incluyen otras funciones</span></div><div class='line' id='LC8'><span class="sd">    que serán útiles.</span></div><div class='line' id='LC9'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC10'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lo</span><span class="p">,</span> <span class="n">hi</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC11'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC12'><span class="sd">        Definimos las propiedades del objeto Intervalo a partir de sus bordes,</span></div><div class='line' id='LC13'><span class="sd">        lo y hi, donde lo &lt;= hi. En el caso en que el intervalo sólo tenga</span></div><div class='line' id='LC14'><span class="sd">        un número, éste se interpreta como un intervalo &#39;delgado&#39; o &#39;degenerado&#39;.</span></div><div class='line' id='LC15'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">hi</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hi</span> <span class="o">=</span> <span class="n">lo</span></div><div class='line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(</span><span class="n">hi</span> <span class="o">&lt;</span> <span class="n">lo</span><span class="p">):</span></div><div class='line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lo</span><span class="p">,</span> <span class="n">hi</span> <span class="o">=</span> <span class="n">hi</span><span class="p">,</span> <span class="n">lo</span></div><div class='line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">=</span> <span class="n">lo</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">=</span> <span class="n">hi</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;Intervalo [{},{}]&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="p">,</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Esta función sirve con &#39;print&#39;</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;[{},{}]&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="p">,</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_repr_html_</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;[{}, {}]&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_repr_latex_</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;$[{}, {}]$&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Aquí vienen las operaciones aritméticas</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__add__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC40'><span class="sd">        Suma de intervalos</span></div><div class='line' id='LC41'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">+</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">+</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span> <span class="o">+</span> <span class="n">Intervalo</span><span class="p">(</span><span class="n">otro</span><span class="p">)</span></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__radd__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span> <span class="o">+</span> <span class="n">otro</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__mul__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mul2</span><span class="p">(</span><span class="n">otro</span><span class="p">)</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_mul1</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">S</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="o">*</span><span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">]</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span> <span class="nb">min</span><span class="p">(</span><span class="n">S</span><span class="p">),</span> <span class="nb">max</span><span class="p">(</span><span class="n">S</span><span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span> <span class="o">*</span> <span class="n">Intervalo</span><span class="p">(</span><span class="n">otro</span><span class="p">)</span></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_mul2</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Multiplicacion de intervalos, evaluando todos los casos posibles &quot;&quot;&quot;</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">&gt;=</span> <span class="mi">0</span> <span class="p">:</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="o">&lt;=</span> <span class="mi">0</span> <span class="p">:</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="o">&lt;=</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span><span class="p">)</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span><span class="p">)</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="o">&lt;=</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span><span class="p">)</span> </div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">&lt;=</span> <span class="mi">0</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span><span class="p">)</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#si no se cumplen las anteriores entonces</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#otro.lo &lt;= 0 &lt;= otro.hi</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="ow">and</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span>   <span class="c">#en este punto se debe tener otro.lo&lt;=0</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">&lt;=</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">:</span>                 <span class="c">#implica que otro.hi&gt;0</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="o">*</span><span class="n">otro</span><span class="o">.</span><span class="n">lo</span><span class="p">))</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span>  <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">:</span>               <span class="c">#tal vez poner 0 &lt;= otro.hi and</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span><span class="p">)</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">&lt;=</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">:</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="o">&gt;=</span><span class="mi">0</span> <span class="p">:</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">,</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span><span class="p">))</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span><span class="p">)</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span> <span class="o">*</span> <span class="n">Intervalo</span><span class="p">(</span><span class="n">otro</span><span class="p">)</span></div><div class='line' id='LC107'><br/></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__rmul__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span> <span class="o">*</span> <span class="n">otro</span></div><div class='line' id='LC111'><br/></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Esta es la funcion igualdad para intervalos</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC115'><span class="sd">        función igualdad para intervalos </span></div><div class='line' id='LC116'><br/></div><div class='line' id='LC117'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">==</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">==</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span><span class="p">:</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">==</span> <span class="n">Intervalo</span><span class="p">(</span><span class="n">otro</span><span class="p">)</span><span class="o">.</span><span class="n">lo</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">==</span> <span class="n">Intervalo</span><span class="p">(</span><span class="n">otro</span><span class="p">)</span><span class="o">.</span><span class="n">hi</span><span class="p">:</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC128'>&nbsp;&nbsp;</div><div class='line' id='LC129'><br/></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#interseccion</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__and__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC133'><span class="sd">        Intersección de intervalos</span></div><div class='line' id='LC134'><span class="sd">        Funciona con la sintaxis &amp; (como el AND bitwise)</span></div><div class='line' id='LC135'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">otro</span><span class="p">,</span><span class="n">Intervalo</span><span class="p">):</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">otro</span> <span class="o">=</span> <span class="n">Intervalo</span><span class="p">(</span><span class="n">otro</span><span class="p">)</span></div><div class='line' id='LC138'><br/></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">&gt;</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span> <span class="o">|</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span> <span class="o">&lt;</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span><span class="p">):</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">None</span></div><div class='line' id='LC141'><br/></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="p">,</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="p">)</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">,</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span> <span class="p">)</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">)</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#interseccion por la izquierda</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__rand__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC150'><span class="sd">        Interseccion de intervalos (por la izquierda)</span></div><div class='line' id='LC151'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span> <span class="o">&amp;</span> <span class="n">otro</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#negativo del intervalo</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__neg__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC157'><span class="sd">        Devuelve el valor negativo del intervalo</span></div><div class='line' id='LC158'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">,</span> <span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="p">)</span></div><div class='line' id='LC160'><br/></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#Funcion reciproco</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">reciprocal</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC164'><span class="sd">        Devuelve un intervalo con los valores recíprocos</span></div><div class='line' id='LC165'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">lo</span> <span class="o">&lt;=</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">:</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#si el intervalo contiene el cero debe de aparecer un error</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">ZeroDivisionError</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="p">(</span><span class="mf">1.0</span><span class="o">/</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">,</span><span class="mf">1.0</span><span class="o">/</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="p">)</span></div><div class='line' id='LC171'><br/></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#division con denominadores que no contienen al cero    </span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__div__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC174'>	<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC175'><span class="sd">	División</span></div><div class='line' id='LC176'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">otro</span><span class="p">,</span> <span class="n">Intervalo</span><span class="p">):</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">otro</span> <span class="o">=</span> <span class="n">Intervalo</span><span class="p">(</span><span class="n">otro</span><span class="p">)</span></div><div class='line' id='LC179'><br/></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">otro</span><span class="o">.</span><span class="n">lo</span> <span class="o">&lt;=</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">otro</span><span class="o">.</span><span class="n">hi</span><span class="p">:</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">ZeroDivisionError</span></div><div class='line' id='LC182'><br/></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span> <span class="o">*</span> <span class="n">otro</span><span class="o">.</span><span class="n">reciprocal</span><span class="p">()</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#división reversa</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__rdiv__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">otro</span><span class="p">):</span></div><div class='line' id='LC188'>	<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC189'><span class="sd">	División revrsa para poder usar floats en el numerador</span></div><div class='line' id='LC190'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">otro</span><span class="p">,</span> <span class="n">Intervalo</span><span class="p">):</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">otro</span> <span class="o">=</span> <span class="n">Intervalo</span><span class="p">(</span><span class="n">otro</span><span class="p">)</span></div><div class='line' id='LC193'><br/></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Intervalo</span><span class="o">.</span><span class="n">__div__</span><span class="p">(</span><span class="n">otro</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">middle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC198'><span class="sd">        Calcula el punto medio del intervalo</span></div><div class='line' id='LC199'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="o">+</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">)</span><span class="o">/</span><span class="mi">2</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">radio</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC204'><span class="sd">        Calcula el radio del intervalo</span></div><div class='line' id='LC205'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="p">)</span><span class="o">/</span><span class="mi">2</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">width</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC210'><span class="sd">        Cacula la anchura</span></div><div class='line' id='LC211'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC212'><br/></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">abs</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">max</span><span class="p">([</span><span class="nb">abs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lo</span><span class="p">),</span><span class="nb">abs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hi</span><span class="p">)])</span></div><div class='line' id='LC218'><br/></div><div class='line' id='LC219'><br/></div></pre></div>
            </td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.06129s from github-fe120-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/ljml27/metodos_rigurosos/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
  </body>
</html>

