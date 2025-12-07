# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

html_sample = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no">
<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Open+Sans:400,600,400italic,700,700italic,600italic,300,300italic,800,800italic">
<link rel="stylesheet" href="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/bootstrap-24col/css/bootstrap.min.css">
<link rel="stylesheet" href="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/css/pangaea.css">
<!--[if lte IE 9]>
<style>#topics-pulldown-wrapper label:after { display:none; }</style>
<![endif]-->
<link rel="shortcut icon" href="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/favicon.ico">
<link rel="icon" href="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/favicon.ico" type="image/vnd.microsoft.icon">
<link rel="image_src" type="image/png" href="https://www.pangaea.de/assets/social-icons/pangaea-share.png">
<meta property="og:image" content="https://www.pangaea.de/assets/social-icons/pangaea-share.png">
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery.matchHeight/0.7.0/jquery.matchHeight-min.js"></script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery.appear/0.4.1/jquery.appear.min.js"></script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js"></script>
<script type="text/javascript" src="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/bootstrap-24col/js/bootstrap.min.js"></script>
<script type="text/javascript" src="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/js/datacombo-min.js"></script>
<title>Huber, R (2019): Maximum diameter of Neogloboquadrina pachyderma sinistral from surface sediment samples from the Norwegian-Greenland Sea</title>
<meta name="title" content="Maximum diameter of Neogloboquadrina pachyderma sinistral from surface sediment samples from the Norwegian-Greenland Sea" />
<meta name="author" content="Huber, Robert" />
<meta name="date" content="2019" />
<meta name="robots" content="index,follow,archive" />
<meta name="description" content="Huber, Robert (2019): Maximum diameter of Neogloboquadrina pachyderma sinistral from surface sediment samples from the Norwegian-Greenland Sea [dataset]. PANGAEA, https://doi.org/10.1594/PANGAEA.908011" />
<meta name="geo.position" content="70.402525;-6.157880" />
<meta name="ICBM" content="70.402525, -6.157880" />
<!--BEGIN: Dublin Core description-->
<link rel="schema.DC" href="http://purl.org/dc/elements/1.1/" />
<link rel="schema.DCTERMS" href="http://purl.org/dc/terms/" />
<meta name="DC.title" content="Maximum diameter of Neogloboquadrina pachyderma sinistral from surface sediment samples from the Norwegian-Greenland Sea" />
<meta name="DC.creator" content="Huber, Robert" />
<meta name="DC.publisher" content="PANGAEA" />
<meta name="DC.date" content="2019" scheme="DCTERMS.W3CDTF" />
<meta name="DC.type" content="Dataset" />
<meta name="DC.language" content="en" scheme="DCTERMS.RFC3066" />
<meta name="DCTERMS.license" scheme="DCTERMS.URI" content="https://creativecommons.org/licenses/by/4.0/" />
<meta name="DC.identifier" content="https://doi.org/10.1594/PANGAEA.908011" scheme="DCTERMS.URI" />
<meta name="DC.rights" scheme="DCTERMS.URI" content="info:eu-repo/semantics/openAccess" />
<meta name="DC.format" content="text/tab-separated-values, 902 data points" />
<!--END: Dublin Core description-->
<script type="text/javascript" src="//maps.googleapis.com/maps/api/js?v=3&amp;language=en&amp;key=AIzaSyByJ17VRKTOT-gTaslZElXnXHPDQp1qKIs"></script>
<script type="text/javascript">/*<![CDATA[*/jQuery(function($) { return initializeSmallDatasetGMap(908011,'hash=f4640ae7d6843a051abdc94b6e958da6',new google.maps.LatLngBounds(new google.maps.LatLng(53.538333333333,-31.086333333333),new google.maps.LatLng(85.3277,15.74933)),undefined); });/*]]>*/</script>
<script type="text/javascript" src="//d1bxh8uas1mnw7.cloudfront.net/assets/embed.js"></script>
<link rel="cite-as" href="https://doi.org/10.1594/PANGAEA.908011">
<link rel="describedby" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=metadata_panmd" type="application/vnd.pangaea.metadata+xml">
<link rel="describedby" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=metadata_datacite4" type="application/vnd.datacite.datacite+xml">
<link rel="describedby" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=citation_bibtex" type="application/x-bibtex">
<link rel="describedby" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=metadata_dif" type="application/vnd.nasa.dif-metadata+xml">
<link rel="describedby" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=citation_text" type="text/x-bibliography">
<link rel="describedby" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=metadata_iso19139" type="application/vnd.iso19139.metadata+xml">
<link rel="describedby" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=citation_ris" type="application/x-research-info-systems">
<link rel="describedby" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=metadata_jsonld" type="application/ld+json">
<link rel="item" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=html" type="text/html">
<link rel="item" href="https://doi.pangaea.de/10.1594/PANGAEA.908011?format=textfile" type="text/tab-separated-values">
<link rel="author" href="https://orcid.org/0000-0003-3000-0020">
<script type="application/ld+json">{"@context":"http://schema.org/","@id":"https://doi.org/10.1594/PANGAEA.908011","@type":"Dataset","identifier":"https://doi.org/10.1594/PANGAEA.908011","url":"https://doi.pangaea.de/10.1594/PANGAEA.908011","creator":{"@id":"https://orcid.org/0000-0003-3000-0020","@type":"Person","name":"Robert Huber","familyName":"Huber","givenName":"Robert","identifier":"https://orcid.org/0000-0003-3000-0020","email":"rhuber@uni-bremen.de"},"name":"Maximum diameter of Neogloboquadrina pachyderma sinistral from surface sediment samples from the Norwegian-Greenland Sea","publisher":{"@type":"Organization","name":"PANGAEA","disambiguatingDescription":"Data Publisher for Earth & Environmental Science","url":"https://www.pangaea.de/"},"includedInDataCatalog":{"@type":"DataCatalog","name":"PANGAEA","disambiguatingDescription":"Data Publisher for Earth & Environmental Science","url":"https://www.pangaea.de/"},"datePublished":"2019-11-01","description":"This data set contains unpublished measurements of the maximum diameter of shells of the planktic foraminifer Neogloboquadrina pachyderma sin. carried out on surface sediment samples from the Norwegian-Greenland Sea.","abstract":"This data set contains unpublished measurements of the maximum diameter of shells of the planktic foraminifer Neogloboquadrina pachyderma sin. carried out on surface sediment samples from the Norwegian-Greenland Sea.","spatialCoverage":{"@type":"Place","geo":{"@type":"GeoShape","box":"53.538333333333 -31.086333333333 85.3277 15.74933","elevation":"-4457.0m/-898.0m"}},"temporalCoverage":"1984-08-10T00:00:00/1993-09-09T00:00:00","size":{"@type":"QuantitativeValue","value":902.0,"unitText":"data points"},"variableMeasured":[{"@type":"PropertyValue","name":"Event label"},{"@type":"PropertyValue","name":"Neogloboquadrina pachyderma sinistral, maximum diameter","unitText":"µm","measurementTechnique":"Scanning electron microscope (SEM)","subjectOf":{"@type":"DefinedTermSet","hasDefinedTerm":[{"@type":"DefinedTerm","name":"maximum"},{"@id":"urn:obo:pato:term:0001334","@type":"DefinedTerm","identifier":"urn:obo:pato:term:0001334","name":"diameter","url":"http://purl.obolibrary.org/obo/PATO_0001334"},{"@id":"http://qudt.org/1.1/vocab/quantity#Length","@type":"DefinedTerm","identifier":"http://qudt.org/1.1/vocab/quantity#Length","name":"Length","alternateName":"L","url":"http://dbpedia.org/resource/Length"}]}}],"license":"https://creativecommons.org/licenses/by/4.0/","conditionsOfAccess":"unrestricted","isAccessibleForFree":true,"inLanguage":"en","distribution":[{"@type":"DataDownload","encodingFormat":"text/html","contentUrl":"https://doi.pangaea.de/10.1594/PANGAEA.908011?format=html"},{"@type":"DataDownload","encodingFormat":"text/tab-separated-values","contentUrl":"https://doi.pangaea.de/10.1594/PANGAEA.908011?format=textfile"}]}</script>
<script type="text/javascript">/*<![CDATA[*/
var _paq=window._paq=window._paq||[];(function(){
var u="https://analytics.pangaea.de/";_paq.push(['setTrackerUrl',u+'matomo.php']);_paq.push(['setCookieDomain','pangaea.de']);_paq.push(['setDomains',['pangaea.de','www.pangaea.de','doi.pangaea.de']]);_paq.push(['setSiteId',1]);
_paq.push(['enableLinkTracking']);_paq.push(['setDownloadClasses',['dl-link']]);_paq.push(['setDownloadExtensions',[]]);_paq.push(['setIgnoreClasses',['notrack']]);_paq.push(['trackPageView']);
var d=document,g=d.createElement('script'),s=d.getElementsByTagName('script')[0];g.async=true;g.src=u+'matomo.js';s.parentNode.insertBefore(g,s);
})();
/*]]>*/</script>
</head>
<body class="homepage-layout">
<div id="header-wrapper">
  <div class="container-fluid">
    <header class="row"><!-- volle Screen-Breite -->
      <div class="content-wrapper"><!-- max. Breite -->
        <div id="login-area-wrapper" class="hidden-print"><div id="login-area"><span id="user-name">Not logged in</span><a id="signup-button" class="glyphicon glyphicon-plus-sign self-referer-link" title="Sign Up / Create Account" aria-label="Sign up" target="_self" rel="nofollow" href="https://www.pangaea.de/user/signup.php?referer=https%3A%2F%2Fdoi.pangaea.de%2F" data-template="https://www.pangaea.de/user/signup.php?referer=#u#"></a><a id="login-button" class="glyphicon glyphicon-log-in self-referer-link" title="Log In" aria-label="Log in" target="_self" rel="nofollow" href="https://www.pangaea.de/user/login.php?referer=https%3A%2F%2Fdoi.pangaea.de%2F" data-template="https://www.pangaea.de/user/login.php?referer=#u#"></a></div></div>
        <div class="blindspalte header-block col-lg-3 col-md-4"></div>
        
        <div id="header-logo-block" class="header-block col-lg-3 col-md-4 col-sm-4 col-xs-8">
          <div id="pangaea-logo">
            <a title="PANGAEA home" href="//www.pangaea.de/" class="home-link"><img src="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/layout-images/pangaea-logo.png" alt="PANGAEA home"></a>
          </div>
        </div>
        
        <div id="header-mid-block" class="header-block col-lg-12 col-md-9 col-sm-20 col-xs-16">
          <div id="pangaea-logo-headline">
            PANGAEA<span class="punkt">.</span>
          </div>
          <div id="pangaea-logo-slogan">
            <span>Data Publisher for Earth &amp; </span><span class="nowrap">Environmental Science</span>
          </div>
          <div id="search-area-header" class="row"></div>
        </div>
        
        <div id="header-main-menu-block" class="header-block hidden-print col-lg-6 col-md-7 col-sm-24 col-xs-24">
          <nav id="main-nav">
            <ul>
              <li id="menu-search">
                <!-- class on link is important, don't change!!! -->
                <a href="//www.pangaea.de/" class="home-link">Search</a>
              </li>
              <li id="menu-submit">
                <a href="//www.pangaea.de/submit/">Submit</a>
              </li>
              <li id="menu-help">
                <a href="//wiki.pangaea.de/">Help</a>
              </li>
              <li id="menu-about">
                <a href="//www.pangaea.de/about/">About</a>
              </li>
              <li id="menu-contact">
                <a href="//www.pangaea.de/contact/">Contact</a>
              </li>
            </ul>
          </nav>
          <div class="clearfix"></div>
        </div>
      </div>
    </header>
  </div>
</div>
<div id="flex-wrapper">
<div id="main-container" class="container-fluid">
<div id="main-row" class="row main-row">
<div id="main" class="col-lg-24 col-md-24 col-sm-24 col-xs-24">
<div id="dataset">
<div class="row"><div class="col-lg-3 col-md-4 col-sm-24 col-xs-24 hidden-xs hidden-sm"><div class="title citation invisible-top-border">Citation:</div>
</div>
<div class="col-lg-21 col-md-20 col-sm-24 col-xs-24"><div class="descr top-border"><div id="gmap-dataset-wrapper" class="gmap-wrapper hidden-print hidden-xs hidden-sm col-lg-8 col-md-8 col-sm-24 col-xs-24"><div class="embed-responsive embed-responsive-4by3"><div id="gmap-dataset" class="embed-responsive-item"></div>
</div>
</div>
<h1 class="hanging citation"><strong><a class="popover-link link-unstyled" href="#" data-title="&lt;span&gt;Huber, Robert&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Huber, Robert'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Huber, Robert'&quot; href=&quot;//www.pangaea.de/?q=author:orcid:0000-0003-3000-0020&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div&gt;&lt;a class=&quot;orcid-link text-nowrap wide-icon-link&quot; target=&quot;_blank&quot; href=&quot;https://orcid.org/0000-0003-3000-0020&quot;&gt;https://orcid.org/0000-0003-3000-0020&lt;/a&gt;&lt;/div&gt;&#10;&lt;div&gt;&lt;a class=&quot;mail-link text-nowrap wide-icon-link&quot; href=&quot;mailto:rhuber@uni-bremen.de&quot;&gt;rhuber@uni-bremen.de&lt;/a&gt;&lt;/div&gt;&#10;&lt;/div&gt;&#10;">Huber, Robert</a> (2019):</strong> Maximum diameter of Neogloboquadrina pachyderma sinistral from surface sediment samples from the Norwegian-Greenland Sea [dataset]. <em>PANGAEA</em>, <a id="citation-doi-link" rel="nofollow bookmark" href="https://doi.org/10.1594/PANGAEA.908011" data-pubstatus="4" class="text-linkwrap popover-link doi-link">https://doi.org/10.1594/PANGAEA.908011</a></h1>
<p class="howtocite"><small><span class="glyphicon glyphicon-bullhorn" aria-hidden="true"></span> <strong>Always quote citation above when using data!</strong> You can download the citation in several formats below.</small></p>
<p class="data-buttons"><a rel="nofollow describedby" title="Export citation to Reference Manager, EndNote, ProCite" href="?format=citation_ris" class="actionbuttonlink"><span class="actionbutton">RIS Citation</span></a><a rel="nofollow describedby" title="Export citation to BibTeX" href="?format=citation_bibtex" class="actionbuttonlink"><span class="actionbutton"><span style="font-variant:small-caps;">BibTeX</span> Citation</span></a><a id="text-citation-link" rel="nofollow" title="Export citation as plain text" href="?format=citation_text" target="_blank" class="actionbuttonlink share-link"><span class="actionbutton">Text Citation</span></a><span class="separator"></span><a rel="nofollow" class="self-referer-link share-link actionbuttonlink" href="//www.pangaea.de/nojs.php" data-template="https://www.facebook.com/sharer.php?u=#u#&amp;t=#t#" title="Share dataset on Facebook" target="_blank"><span class="actionbutton"><span class="glyphicon glyphicon-share"></span> Facebook</span></a><a rel="nofollow" class="self-referer-link share-link actionbuttonlink" href="//www.pangaea.de/nojs.php" data-template="https://twitter.com/intent/tweet?url=#u#&amp;text=#t#&amp;via=PANGAEAdataPubl" title="Share dataset on Twitter" target="_blank"><span class="actionbutton"><span class="glyphicon glyphicon-share"></span> Twitter</span></a><span class="separator"></span><a rel="nofollow" target="_blank" title="Display events in map" href="//www.pangaea.de/advanced/gmap-dataset.php?id=908011&amp;viewportBBOX=-31.086333333333,53.538333333333,15.74933,85.3277" class="actionbuttonlink"><span class="actionbutton">Show Map</span></a><a rel="nofollow" title="Display events in Google Earth" href="?format=events_kml" class="actionbuttonlink"><span class="actionbutton">Google Earth</span></a><span data-badge-type="1" data-doi="10.1594/PANGAEA.908011" data-badge-popover="right" data-hide-no-mentions="true" class="altmetric-embed sep-before"></span><span class="sep-before" id="usage-stats"></span></p>
<div class="clearfix"></div>
</div>
</div>
</div>
<div class="row"><div class="col-lg-3 col-md-4 col-sm-24 col-xs-24"><div class="title">Abstract:</div>
</div>
<div class="col-lg-21 col-md-20 col-sm-24 col-xs-24"><div class="descr"><div class="abstract">This data set contains unpublished measurements of the maximum diameter of shells of the planktic foraminifer Neogloboquadrina pachyderma sin. carried out on surface sediment samples from the Norwegian-Greenland Sea.</div>
</div>
</div>
</div>
<div class="row"><div class="col-lg-3 col-md-4 col-sm-24 col-xs-24"><div class="title">Project(s):</div>
</div>
<div class="col-lg-21 col-md-20 col-sm-24 col-xs-24"><div class="descr"><div class="hanging"><strong><a href="//www.pangaea.de/nojs.php" class="popover-link" data-title="&lt;span&gt;Veränderungen pelagischer Karbonatflüsse seit dem Pliozän: Rekonstruktion polarer und atlantischer Wassermassen im Nordatlantik&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Veränderungen pelagischer Karbonatflüsse seit dem Pliozän: Rekonstruktion polarer und atlantischer Wassermassen im Nordatlantik'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Veränderungen pelagischer Karbonatflüsse seit dem Pliozän: Rekonstruktion polarer und atlantischer Wassermassen im Nordatlantik'&quot; href=&quot;//www.pangaea.de/?q=project:label:PlioKarbonat&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Label:&lt;/strong&gt; PlioKarbonat&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Institution:&lt;/strong&gt; &lt;span&gt;&lt;a target=&quot;_blank&quot; href=&quot;http://www.geo.uni-bremen.de/page.php?langid=EN&quot;&gt;Department of Geosciences, Bremen University&lt;/a&gt;&lt;/span&gt; (GeoB, &lt;a class=&quot;text-linkwrap ror-link&quot; href=&quot;https://ror.org/04ers2y35&quot; target=&quot;_blank&quot;&gt;https://ror.org/04ers2y35&lt;/a&gt;)&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Department of Geosciences, Bremen University'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Department of Geosciences, Bremen University'&quot; href=&quot;//www.pangaea.de/?q=institution:ror:https:%2F%2Fror.org%2F04ers2y35&quot;&gt;&lt;/a&gt;&lt;/div&gt;&#10;&lt;/div&gt;&#10;">Veränderungen pelagischer Karbonatflüsse seit dem Pliozän: Rekonstruktion polarer und atlantischer Wassermassen im Nordatlantik</a></strong> (PlioKarbonat)<a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Veränderungen pelagischer Karbonatflüsse seit dem Pliozän: Rekonstruktion polarer und atlantischer Wassermassen im Nordatlantik'..." aria-label="Search PANGAEA for other datasets related to 'Veränderungen pelagischer Karbonatflüsse seit dem Pliozän: Rekonstruktion polarer und atlantischer Wassermassen im Nordatlantik'" href="//www.pangaea.de/?q=project:label:PlioKarbonat"></a></div>
</div>
</div>
</div>
<div class="row"><div class="col-lg-3 col-md-4 col-sm-24 col-xs-24"><div class="title">Coverage:</div>
</div>
<div class="col-lg-21 col-md-20 col-sm-24 col-xs-24"><div class="descr"><div class="hanging geo"><em class="unfarbe">Median Latitude: </em><span class="latitude">70.402525</span><em class="unfarbe"> * Median Longitude: </em><span class="longitude">-6.157880</span><em class="unfarbe"> * South-bound Latitude: </em>53.538333<em class="unfarbe"> * West-bound Longitude: </em>-31.086333<em class="unfarbe"> * North-bound Latitude: </em>85.327700<em class="unfarbe"> * East-bound Longitude: </em>15.749330</div>
<div class="hanging"><em class="unfarbe">Date/Time Start: </em>1984-08-10T00:00:00<em class="unfarbe"> * Date/Time End: </em>1993-09-09T00:00:00</div>
<div class="hanging"><em class="unfarbe">Minimum Elevation: </em>-4457.0 <span class="unit">m</span><em class="unfarbe"> * Maximum Elevation: </em>-898.0 <span class="unit">m</span></div>
</div>
</div>
</div>
<div class="row"><div class="col-lg-3 col-md-4 col-sm-24 col-xs-24"><div class="title">Event(s):</div>
</div>
<div class="col-lg-21 col-md-20 col-sm-24 col-xs-24"><div class="descr"><div class="hanging geo"><strong>GIK23061-3</strong><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'GIK23061-3'..." aria-label="Search PANGAEA for other datasets related to 'GIK23061-3'" href="//www.pangaea.de/?q=event:label:GIK23061-3"></a><em class="unfarbe"> * Latitude: </em><span class="latitude">69.501667</span><em class="unfarbe"> * Longitude: </em><span class="longitude">-2.028333</span><em class="unfarbe"> * Date/Time: </em>1986-07-07T00:00:00<em class="unfarbe"> * Elevation: </em>-3534.0 <span class="unit">m</span><em class="unfarbe"> * Location: </em><span>Norwegian Sea</span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Norwegian Sea'..." aria-label="Search PANGAEA for other datasets related to 'Norwegian Sea'" href="//www.pangaea.de/?q=location:%22Norwegian%20Sea%22"></a><em class="unfarbe"> * Campaign: </em><span><a target="_blank" href="https://doi.org/10.2312/cr_m2" class="popover-link" data-title="&lt;span&gt;Campaign: &lt;a target=&quot;_blank&quot; href=&quot;https://doi.org/10.2312/cr_m2&quot;&gt;M2/2&lt;/a&gt;&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'M2/2'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'M2/2'&quot; href=&quot;//www.pangaea.de/?q=campaign:%22M2%2F2%22&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Event list:&lt;/strong&gt; &lt;a href=&quot;//www.pangaea.de/expeditions/events/M2%2F2&quot;&gt;Link&lt;/a&gt;&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Chief Scientist(s):&lt;/strong&gt; Thiede, Jörn&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Cruise Report:&lt;/strong&gt; &lt;a class=&quot;text-linkwrap doi-link&quot; href=&quot;https://doi.org/10.2312/cr_m2&quot; target=&quot;_blank&quot;&gt;https://doi.org/10.2312/cr_m2&lt;/a&gt;&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Start:&lt;/strong&gt; 1986-07-03&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;End:&lt;/strong&gt; 1986-07-16&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Start location:&lt;/strong&gt; Trondheim, Norway&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;End location:&lt;/strong&gt; Bremerhaven&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;BSH ID:&lt;/strong&gt; 19870096&lt;/div&gt;&#10;&lt;/div&gt;&#10;">M2/2</a></span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'M2/2'..." aria-label="Search PANGAEA for other datasets related to 'M2/2'" href="//www.pangaea.de/?q=campaign:%22M2%2F2%22"></a><em class="unfarbe"> * Basis: </em><span><a target="_blank" href="https://en.wikipedia.org/wiki/RV_Meteor_(1986)" class="popover-link" data-title="&lt;span&gt;Basis: &lt;a target=&quot;_blank&quot; href=&quot;https://en.wikipedia.org/wiki/RV_Meteor_(1986)&quot;&gt;Meteor (1986)&lt;/a&gt;&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Meteor (1986)'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Meteor (1986)'&quot; href=&quot;//www.pangaea.de/?q=basis:%22Meteor%20(1986)%22&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Call Sign:&lt;/strong&gt; DBBH&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;IMO number:&lt;/strong&gt; 8411279&lt;/div&gt;&#10;&lt;/div&gt;&#10;">Meteor (1986)</a></span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Meteor (1986)'..." aria-label="Search PANGAEA for other datasets related to 'Meteor (1986)'" href="//www.pangaea.de/?q=basis:%22Meteor%20(1986)%22"></a><em class="unfarbe"> * Method/Device: </em><span><a target="_blank" href="http://en.wikipedia.org/wiki/Box_corer">Giant box corer</a></span> (GKG)<a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Giant box corer'..." aria-label="Search PANGAEA for other datasets related to 'Giant box corer'" href="//www.pangaea.de/?q=method:%22Giant%20box%20corer%22"></a></div>
<div class="hanging geo"><strong>GIK23063-2</strong><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'GIK23063-2'..." aria-label="Search PANGAEA for other datasets related to 'GIK23063-2'" href="//www.pangaea.de/?q=event:label:GIK23063-2"></a><em class="unfarbe"> * Latitude: </em><span class="latitude">68.746667</span><em class="unfarbe"> * Longitude: </em><span class="longitude">-0.005000</span><em class="unfarbe"> * Date/Time: </em>1986-07-08T00:00:00<em class="unfarbe"> * Elevation: </em>-2302.0 <span class="unit">m</span><em class="unfarbe"> * Recovery: </em>0.35 m<em class="unfarbe"> * Location: </em><span>Norwegian Sea</span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Norwegian Sea'..." aria-label="Search PANGAEA for other datasets related to 'Norwegian Sea'" href="//www.pangaea.de/?q=location:%22Norwegian%20Sea%22"></a><em class="unfarbe"> * Campaign: </em><span><a target="_blank" href="https://doi.org/10.2312/cr_m2" class="popover-link" data-title="&lt;span&gt;Campaign: &lt;a target=&quot;_blank&quot; href=&quot;https://doi.org/10.2312/cr_m2&quot;&gt;M2/2&lt;/a&gt;&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'M2/2'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'M2/2'&quot; href=&quot;//www.pangaea.de/?q=campaign:%22M2%2F2%22&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Event list:&lt;/strong&gt; &lt;a href=&quot;//www.pangaea.de/expeditions/events/M2%2F2&quot;&gt;Link&lt;/a&gt;&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Chief Scientist(s):&lt;/strong&gt; Thiede, Jörn&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Cruise Report:&lt;/strong&gt; &lt;a class=&quot;text-linkwrap doi-link&quot; href=&quot;https://doi.org/10.2312/cr_m2&quot; target=&quot;_blank&quot;&gt;https://doi.org/10.2312/cr_m2&lt;/a&gt;&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Start:&lt;/strong&gt; 1986-07-03&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;End:&lt;/strong&gt; 1986-07-16&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Start location:&lt;/strong&gt; Trondheim, Norway&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;End location:&lt;/strong&gt; Bremerhaven&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;BSH ID:&lt;/strong&gt; 19870096&lt;/div&gt;&#10;&lt;/div&gt;&#10;">M2/2</a></span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'M2/2'..." aria-label="Search PANGAEA for other datasets related to 'M2/2'" href="//www.pangaea.de/?q=campaign:%22M2%2F2%22"></a><em class="unfarbe"> * Basis: </em><span><a target="_blank" href="https://en.wikipedia.org/wiki/RV_Meteor_(1986)" class="popover-link" data-title="&lt;span&gt;Basis: &lt;a target=&quot;_blank&quot; href=&quot;https://en.wikipedia.org/wiki/RV_Meteor_(1986)&quot;&gt;Meteor (1986)&lt;/a&gt;&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Meteor (1986)'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Meteor (1986)'&quot; href=&quot;//www.pangaea.de/?q=basis:%22Meteor%20(1986)%22&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Call Sign:&lt;/strong&gt; DBBH&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;IMO number:&lt;/strong&gt; 8411279&lt;/div&gt;&#10;&lt;/div&gt;&#10;">Meteor (1986)</a></span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Meteor (1986)'..." aria-label="Search PANGAEA for other datasets related to 'Meteor (1986)'" href="//www.pangaea.de/?q=basis:%22Meteor%20(1986)%22"></a><em class="unfarbe"> * Method/Device: </em><span><a target="_blank" href="http://en.wikipedia.org/wiki/Box_corer">Giant box corer</a></span> (GKG)<a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Giant box corer'..." aria-label="Search PANGAEA for other datasets related to 'Giant box corer'" href="//www.pangaea.de/?q=method:%22Giant%20box%20corer%22"></a></div>
<div class="hanging geo"><strong>GIK23069-2</strong><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'GIK23069-2'..." aria-label="Search PANGAEA for other datasets related to 'GIK23069-2'" href="//www.pangaea.de/?q=event:label:GIK23069-2"></a><em class="unfarbe"> * Latitude: </em><span class="latitude">67.665000</span><em class="unfarbe"> * Longitude: </em><span class="longitude">1.600000</span><em class="unfarbe"> * Date/Time: </em>1986-07-11T00:00:00<em class="unfarbe"> * Elevation: </em>-1894.0 <span class="unit">m</span><em class="unfarbe"> * Location: </em><span>Norwegian Sea</span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Norwegian Sea'..." aria-label="Search PANGAEA for other datasets related to 'Norwegian Sea'" href="//www.pangaea.de/?q=location:%22Norwegian%20Sea%22"></a><em class="unfarbe"> * Campaign: </em><span><a target="_blank" href="https://doi.org/10.2312/cr_m2" class="popover-link" data-title="&lt;span&gt;Campaign: &lt;a target=&quot;_blank&quot; href=&quot;https://doi.org/10.2312/cr_m2&quot;&gt;M2/2&lt;/a&gt;&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'M2/2'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'M2/2'&quot; href=&quot;//www.pangaea.de/?q=campaign:%22M2%2F2%22&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Event list:&lt;/strong&gt; &lt;a href=&quot;//www.pangaea.de/expeditions/events/M2%2F2&quot;&gt;Link&lt;/a&gt;&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Chief Scientist(s):&lt;/strong&gt; Thiede, Jörn&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Cruise Report:&lt;/strong&gt; &lt;a class=&quot;text-linkwrap doi-link&quot; href=&quot;https://doi.org/10.2312/cr_m2&quot; target=&quot;_blank&quot;&gt;https://doi.org/10.2312/cr_m2&lt;/a&gt;&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Start:&lt;/strong&gt; 1986-07-03&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;End:&lt;/strong&gt; 1986-07-16&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Start location:&lt;/strong&gt; Trondheim, Norway&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;End location:&lt;/strong&gt; Bremerhaven&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;BSH ID:&lt;/strong&gt; 19870096&lt;/div&gt;&#10;&lt;/div&gt;&#10;">M2/2</a></span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'M2/2'..." aria-label="Search PANGAEA for other datasets related to 'M2/2'" href="//www.pangaea.de/?q=campaign:%22M2%2F2%22"></a><em class="unfarbe"> * Basis: </em><span><a target="_blank" href="https://en.wikipedia.org/wiki/RV_Meteor_(1986)" class="popover-link" data-title="&lt;span&gt;Basis: &lt;a target=&quot;_blank&quot; href=&quot;https://en.wikipedia.org/wiki/RV_Meteor_(1986)&quot;&gt;Meteor (1986)&lt;/a&gt;&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Meteor (1986)'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Meteor (1986)'&quot; href=&quot;//www.pangaea.de/?q=basis:%22Meteor%20(1986)%22&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Call Sign:&lt;/strong&gt; DBBH&lt;/div&gt;&#10;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;IMO number:&lt;/strong&gt; 8411279&lt;/div&gt;&#10;&lt;/div&gt;&#10;">Meteor (1986)</a></span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Meteor (1986)'..." aria-label="Search PANGAEA for other datasets related to 'Meteor (1986)'" href="//www.pangaea.de/?q=basis:%22Meteor%20(1986)%22"></a><em class="unfarbe"> * Method/Device: </em><span><a target="_blank" href="http://en.wikipedia.org/wiki/Box_corer">Giant box corer</a></span> (GKG)<a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Giant box corer'..." aria-label="Search PANGAEA for other datasets related to 'Giant box corer'" href="//www.pangaea.de/?q=method:%22Giant%20box%20corer%22"></a></div>
<div class="metadata-expander"><div class="expander-wrapper"><a rel="nofollow" href="//www.pangaea.de/nojs.php" data-format="metadata_hidden_events" class="target-hide"></a><span class="toggle-status"></span></div>
<div class="metadata-expand-target"></div>
</div>
</div>
</div>
</div>
<div class="row"><div class="col-lg-3 col-md-4 col-sm-24 col-xs-24"><div class="title">Parameter(s):</div>
</div>
<div class="col-lg-21 col-md-20 col-sm-24 col-xs-24"><div class="descr"><div class="table-responsive"><table class="parametertable"><tr><th class="colno">#</th><th>Name</th><th>Short Name</th><th>Unit</th><th>Principal Investigator</th><th>Method/Device</th><th>Comment</th></tr>
<tr title="Event" id="lcol0_ds13774074"><td class="colno"><span class="colno">1</span></td><td><span>Event label</span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Event label'..." aria-label="Search PANGAEA for other datasets related to 'Event label'" href="//www.pangaea.de/?q=parameter:%22Event%20label%22"></a></td><td>Event</td><td></td><td><a class="popover-link" href="https://orcid.org/0000-0003-3000-0020" data-title="&lt;span&gt;Huber, Robert&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Huber, Robert'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Huber, Robert'&quot; href=&quot;//www.pangaea.de/?q=PI:orcid:0000-0003-3000-0020&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div&gt;&lt;a class=&quot;orcid-link text-nowrap wide-icon-link&quot; target=&quot;_blank&quot; href=&quot;https://orcid.org/0000-0003-3000-0020&quot;&gt;https://orcid.org/0000-0003-3000-0020&lt;/a&gt;&lt;/div&gt;&#10;&lt;div&gt;&lt;a class=&quot;mail-link text-nowrap wide-icon-link&quot; href=&quot;mailto:rhuber@uni-bremen.de&quot;&gt;rhuber@uni-bremen.de&lt;/a&gt;&lt;/div&gt;&#10;&lt;/div&gt;&#10;">Huber, Robert</a><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Huber, Robert'..." aria-label="Search PANGAEA for other datasets related to 'Huber, Robert'" href="//www.pangaea.de/?q=PI:orcid:0000-0003-3000-0020"></a></td><td></td><td></td></tr>
<tr title="N. pachyderma s max diam [µm]" id="lcol1_ds13774075"><td class="colno"><span class="colno">2</span></td><td><span><a href="//www.pangaea.de/nojs.php" class="popover-link" data-title="&lt;span&gt;&lt;span&gt;Neogloboquadrina pachyderma sinistral, &lt;/span&gt;&lt;span class=&quot;text-termcolor1&quot; id=&quot;col1.ds13774075.param20708.term38492&quot;&gt;maximum&lt;/span&gt;&lt;span&gt; &lt;/span&gt;&lt;span class=&quot;text-termcolor2&quot; id=&quot;col1.ds13774075.param20708.term1073584&quot;&gt;diameter&lt;/span&gt; [&lt;span class=&quot;text-termcolor3&quot;&gt;&lt;span class=&quot;unit&quot;&gt;µm&lt;/span&gt;&lt;/span&gt;]&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Neogloboquadrina pachyderma sinistral, maximum diameter'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Neogloboquadrina pachyderma sinistral, maximum diameter'&quot; href=&quot;//www.pangaea.de/?q=parameter:%22Neogloboquadrina%20pachyderma%20sinistral,%20maximum%20diameter%22&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div class=&quot;popover-mitem&quot;&gt;&lt;strong&gt;Short name:&lt;/strong&gt; N. pachyderma s max diam [&lt;span class=&quot;unit&quot;&gt;µm&lt;/span&gt;]&lt;/div&gt;&#10;&lt;p class=&quot;text-bold&quot;&gt;Terms used:&lt;/p&gt;&#10;&lt;ul class=&quot;termlist&quot; role=&quot;list&quot;&gt;&lt;li class=&quot;item-termcolor1&quot;&gt;&lt;span&gt;maximum&lt;/span&gt;&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'maximum'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'maximum'&quot; href=&quot;//www.pangaea.de/?q=term:%22maximum%22&quot;&gt;&lt;/a&gt;&lt;/li&gt;&#10;&lt;li class=&quot;item-termcolor2&quot;&gt;&lt;span&gt;&lt;a target=&quot;_blank&quot; href=&quot;http://purl.obolibrary.org/obo/PATO_0001334&quot;&gt;diameter&lt;/a&gt;&lt;/span&gt; (&lt;code class=&quot;text-linkwrap&quot;&gt;urn:obo:pato:term:0001334&lt;/code&gt;)&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'diameter'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'diameter'&quot; href=&quot;//www.pangaea.de/?q=relateduri:urn:obo:pato:term:0001334&quot;&gt;&lt;/a&gt;&lt;/li&gt;&#10;&lt;li class=&quot;item-termcolor3&quot;&gt;&lt;span&gt;&lt;a target=&quot;_blank&quot; href=&quot;http://dbpedia.org/resource/Length&quot;&gt;Length&lt;/a&gt;&lt;/span&gt; (L, &lt;code class=&quot;text-linkwrap&quot;&gt;http://qudt.org/1.1/vocab/quantity#Length&lt;/code&gt;)&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Length'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Length'&quot; href=&quot;//www.pangaea.de/?q=relateduri:http:%2F%2Fqudt.org%2F1.1%2Fvocab%2Fquantity%23Length&quot;&gt;&lt;/a&gt;&lt;/li&gt;&#10;&lt;/ul&gt;&#10;&lt;p class=&quot;text-italic&quot;&gt;This is a beta feature. Please &lt;a href=&quot;//www.pangaea.de/contact/&quot;&gt;report&lt;/a&gt; any incorrect term assignments.&lt;/p&gt;&#10;&lt;/div&gt;&#10;">Neogloboquadrina pachyderma sinistral, maximum diameter</a></span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Neogloboquadrina pachyderma sinistral, maximum diameter'..." aria-label="Search PANGAEA for other datasets related to 'Neogloboquadrina pachyderma sinistral, maximum diameter'" href="//www.pangaea.de/?q=parameter:%22Neogloboquadrina%20pachyderma%20sinistral,%20maximum%20diameter%22"></a></td><td>N. pachyderma s max diam</td><td><span class="unit">µm</span></td><td><a class="popover-link" href="https://orcid.org/0000-0003-3000-0020" data-title="&lt;span&gt;Huber, Robert&lt;a class=&quot;searchlink glyphicon glyphicon-search&quot; target=&quot;_blank&quot; rel=&quot;nofollow&quot; title=&quot;Search PANGAEA for other datasets related to 'Huber, Robert'...&quot; aria-label=&quot;Search PANGAEA for other datasets related to 'Huber, Robert'&quot; href=&quot;//www.pangaea.de/?q=PI:orcid:0000-0003-3000-0020&quot;&gt;&lt;/a&gt;&lt;/span&gt;" data-content="&lt;div&gt;&lt;div&gt;&lt;a class=&quot;orcid-link text-nowrap wide-icon-link&quot; target=&quot;_blank&quot; href=&quot;https://orcid.org/0000-0003-3000-0020&quot;&gt;https://orcid.org/0000-0003-3000-0020&lt;/a&gt;&lt;/div&gt;&#10;&lt;div&gt;&lt;a class=&quot;mail-link text-nowrap wide-icon-link&quot; href=&quot;mailto:rhuber@uni-bremen.de&quot;&gt;rhuber@uni-bremen.de&lt;/a&gt;&lt;/div&gt;&#10;&lt;/div&gt;&#10;">Huber, Robert</a><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Huber, Robert'..." aria-label="Search PANGAEA for other datasets related to 'Huber, Robert'" href="//www.pangaea.de/?q=PI:orcid:0000-0003-3000-0020"></a></td><td><span><a target="_blank" href="https://en.wikipedia.org/wiki/Scanning_electron_microscope">Scanning electron microscope (SEM)</a></span><a class="searchlink glyphicon glyphicon-search" target="_blank" rel="nofollow" title="Search PANGAEA for other datasets related to 'Scanning electron microscope (SEM)'..." aria-label="Search PANGAEA for other datasets related to 'Scanning electron microscope (SEM)'" href="//www.pangaea.de/?q=method:%22Scanning%20electron%20microscope%20(SEM)%22"></a></td><td></td></tr>
</table>
</div>
</div>
</div>
</div>
<div class="row"><div class="col-lg-3 col-md-4 col-sm-24 col-xs-24"><div class="title">License:</div>
</div>
<div class="col-lg-21 col-md-20 col-sm-24 col-xs-24"><div class="descr"><div class="hanging"><span><a href="https://creativecommons.org/licenses/by/4.0/" class="license-icon-CC-BY" rel="license" target="_blank">Creative Commons Attribution 4.0 International</a> (CC-BY-4.0)</span></div>
</div>
</div>
</div>
<div class="row"><div class="col-lg-3 col-md-4 col-sm-24 col-xs-24"><div class="title">Size:</div>
</div>
<div class="col-lg-21 col-md-20 col-sm-24 col-xs-24"><div class="descr"><div class="hanging">902 data points</div>
</div>
</div>
</div>
<div class="row"><div class="col-lg-21 col-md-20 col-sm-24 col-xs-24 col-lg-offset-3 col-md-offset-4"><div class="text-block top-border">
<h2 id="download">Download Data</h2>
<form name="dd" action="/10.1594/PANGAEA.908011" method="get" target="_self"><p><a rel="nofollow" id="download-link" class="dl-link" href="?format=textfile">Download dataset as tab-delimited text</a> <small><em>&mdash; use the following character encoding:</em> <input type="hidden" name="format" value="textfile" /><select id="contr_charset" name="charset" size="1" onchange="setCharsetCookie(this.options[this.selectedIndex].value)" style="font-size: 8pt"><optgroup label="most used"><option selected="selected" value="UTF-8">UTF-8: Unicode (PANGAEA default)</option><option value="ISO-8859-1">ISO-8859-1: ISO Western</option><option value="windows-1252">windows-1252: Windows Western</option><option value="x-MacRoman">x-MacRoman: Macintosh Roman</option><option value="IBM437">IBM437: MS-DOS compatible, United States</option><option value="IBM850">IBM850: MS-DOS compatible, Western</option></optgroup><optgroup label="others (warning: missing characters may get replaced by ?)"><option value="Big5">Big5</option><option value="Big5-HKSCS">Big5-HKSCS</option><option value="CESU-8">CESU-8</option><option value="EUC-JP">EUC-JP</option><option value="EUC-KR">EUC-KR</option><option value="GB18030">GB18030</option><option value="GB2312">GB2312</option><option value="GBK">GBK</option><option value="IBM-Thai">IBM-Thai</option><option value="IBM00858">IBM00858</option><option value="IBM01140">IBM01140</option><option value="IBM01141">IBM01141</option><option value="IBM01142">IBM01142</option><option value="IBM01143">IBM01143</option><option value="IBM01144">IBM01144</option><option value="IBM01145">IBM01145</option><option value="IBM01146">IBM01146</option><option value="IBM01147">IBM01147</option><option value="IBM01148">IBM01148</option><option value="IBM01149">IBM01149</option><option value="IBM037">IBM037</option><option value="IBM1026">IBM1026</option><option value="IBM1047">IBM1047</option><option value="IBM273">IBM273</option><option value="IBM277">IBM277</option><option value="IBM278">IBM278</option><option value="IBM280">IBM280</option><option value="IBM284">IBM284</option><option value="IBM285">IBM285</option><option value="IBM290">IBM290</option><option value="IBM297">IBM297</option><option value="IBM420">IBM420</option><option value="IBM424">IBM424</option><option value="IBM500">IBM500</option><option value="IBM775">IBM775</option><option value="IBM852">IBM852</option><option value="IBM855">IBM855</option><option value="IBM857">IBM857</option><option value="IBM860">IBM860</option><option value="IBM861">IBM861</option><option value="IBM862">IBM862</option><option value="IBM863">IBM863</option><option value="IBM864">IBM864</option><option value="IBM865">IBM865</option><option value="IBM866">IBM866</option><option value="IBM868">IBM868</option><option value="IBM869">IBM869</option><option value="IBM870">IBM870</option><option value="IBM871">IBM871</option><option value="IBM918">IBM918</option><option value="ISO-2022-JP">ISO-2022-JP</option><option value="ISO-2022-JP-2">ISO-2022-JP-2</option><option value="ISO-2022-KR">ISO-2022-KR</option><option value="ISO-8859-13">ISO-8859-13</option><option value="ISO-8859-15">ISO-8859-15</option><option value="ISO-8859-16">ISO-8859-16</option><option value="ISO-8859-2">ISO-8859-2</option><option value="ISO-8859-3">ISO-8859-3</option><option value="ISO-8859-4">ISO-8859-4</option><option value="ISO-8859-5">ISO-8859-5</option><option value="ISO-8859-6">ISO-8859-6</option><option value="ISO-8859-7">ISO-8859-7</option><option value="ISO-8859-8">ISO-8859-8</option><option value="ISO-8859-9">ISO-8859-9</option><option value="JIS_X0201">JIS_X0201</option><option value="JIS_X0212-1990">JIS_X0212-1990</option><option value="KOI8-R">KOI8-R</option><option value="KOI8-U">KOI8-U</option><option value="Shift_JIS">Shift_JIS</option><option value="TIS-620">TIS-620</option><option value="US-ASCII">US-ASCII</option><option value="UTF-16">UTF-16</option><option value="UTF-16BE">UTF-16BE</option><option value="UTF-16LE">UTF-16LE</option><option value="UTF-32">UTF-32</option><option value="UTF-32BE">UTF-32BE</option><option value="UTF-32LE">UTF-32LE</option><option value="windows-1250">windows-1250</option><option value="windows-1251">windows-1251</option><option value="windows-1253">windows-1253</option><option value="windows-1254">windows-1254</option><option value="windows-1255">windows-1255</option><option value="windows-1256">windows-1256</option><option value="windows-1257">windows-1257</option><option value="windows-1258">windows-1258</option><option value="windows-31j">windows-31j</option><option value="x-Big5-HKSCS-2001">x-Big5-HKSCS-2001</option><option value="x-Big5-Solaris">x-Big5-Solaris</option><option value="x-euc-jp-linux">x-euc-jp-linux</option><option value="x-EUC-TW">x-EUC-TW</option><option value="x-eucJP-Open">x-eucJP-Open</option><option value="x-IBM1006">x-IBM1006</option><option value="x-IBM1025">x-IBM1025</option><option value="x-IBM1046">x-IBM1046</option><option value="x-IBM1097">x-IBM1097</option><option value="x-IBM1098">x-IBM1098</option><option value="x-IBM1112">x-IBM1112</option><option value="x-IBM1122">x-IBM1122</option><option value="x-IBM1123">x-IBM1123</option><option value="x-IBM1124">x-IBM1124</option><option value="x-IBM1129">x-IBM1129</option><option value="x-IBM1166">x-IBM1166</option><option value="x-IBM1364">x-IBM1364</option><option value="x-IBM1381">x-IBM1381</option><option value="x-IBM1383">x-IBM1383</option><option value="x-IBM29626C">x-IBM29626C</option><option value="x-IBM300">x-IBM300</option><option value="x-IBM33722">x-IBM33722</option><option value="x-IBM737">x-IBM737</option><option value="x-IBM833">x-IBM833</option><option value="x-IBM834">x-IBM834</option><option value="x-IBM856">x-IBM856</option><option value="x-IBM874">x-IBM874</option><option value="x-IBM875">x-IBM875</option><option value="x-IBM921">x-IBM921</option><option value="x-IBM922">x-IBM922</option><option value="x-IBM930">x-IBM930</option><option value="x-IBM933">x-IBM933</option><option value="x-IBM935">x-IBM935</option><option value="x-IBM937">x-IBM937</option><option value="x-IBM939">x-IBM939</option><option value="x-IBM942">x-IBM942</option><option value="x-IBM942C">x-IBM942C</option><option value="x-IBM943">x-IBM943</option><option value="x-IBM943C">x-IBM943C</option><option value="x-IBM948">x-IBM948</option><option value="x-IBM949">x-IBM949</option><option value="x-IBM949C">x-IBM949C</option><option value="x-IBM950">x-IBM950</option><option value="x-IBM964">x-IBM964</option><option value="x-IBM970">x-IBM970</option><option value="x-ISCII91">x-ISCII91</option><option value="x-ISO-2022-CN-CNS">x-ISO-2022-CN-CNS</option><option value="x-ISO-2022-CN-GB">x-ISO-2022-CN-GB</option><option value="x-iso-8859-11">x-iso-8859-11</option><option value="x-JIS0208">x-JIS0208</option><option value="x-Johab">x-Johab</option><option value="x-MacArabic">x-MacArabic</option><option value="x-MacCentralEurope">x-MacCentralEurope</option><option value="x-MacCroatian">x-MacCroatian</option><option value="x-MacCyrillic">x-MacCyrillic</option><option value="x-MacDingbat">x-MacDingbat</option><option value="x-MacGreek">x-MacGreek</option><option value="x-MacHebrew">x-MacHebrew</option><option value="x-MacIceland">x-MacIceland</option><option value="x-MacRomania">x-MacRomania</option><option value="x-MacSymbol">x-MacSymbol</option><option value="x-MacThai">x-MacThai</option><option value="x-MacTurkish">x-MacTurkish</option><option value="x-MacUkraine">x-MacUkraine</option><option value="x-MS932_0213">x-MS932_0213</option><option value="x-MS950-HKSCS">x-MS950-HKSCS</option><option value="x-MS950-HKSCS-XP">x-MS950-HKSCS-XP</option><option value="x-mswin-936">x-mswin-936</option><option value="x-PCK">x-PCK</option><option value="x-SJIS_0213">x-SJIS_0213</option><option value="x-UTF-16LE-BOM">x-UTF-16LE-BOM</option><option value="X-UTF-32BE-BOM">X-UTF-32BE-BOM</option><option value="X-UTF-32LE-BOM">X-UTF-32LE-BOM</option><option value="x-windows-50220">x-windows-50220</option><option value="x-windows-50221">x-windows-50221</option><option value="x-windows-874">x-windows-874</option><option value="x-windows-949">x-windows-949</option><option value="x-windows-950">x-windows-950</option><option value="x-windows-iso2022jp">x-windows-iso2022jp</option></optgroup></select>
</small></p></form>
<p><a rel="nofollow" class="view-link" href="?format=html#download" target="_self">View dataset as HTML</a></p>
</div></div></div><div id="recommendations"></div>
</div>
</div>
</div>
</div>
</div>
<div id="footer-wrapper" class="top-border hidden-print">
  <div class="container-fluid">
    <footer class="row"><!-- volle Screen-Breite -->
      <div class="content-wrapper"><!-- max. Breite -->
        <div class="blindspalte col-lg-3 col-md-4 col-sm-4 col-xs-4"></div>
        <div id="footer-hosted-by-area" class="col-lg-18 col-md-9 col-sm-24 col-xs-24">
          <div class="col-lg-12 col-md-24 col-sm-24 col-xs-24">
            <div class="headline underlined">
              PANGAEA is hosted by
            </div>
            
            <div>
              <p>
                Alfred Wegener Institute, Helmholtz Center for Polar and Marine Research (AWI)<br/>
                Center for Marine Environmental Sciences, University of Bremen (MARUM)
              </p>
            </div>

            <div class="headline underlined">
              The System is supported by
            </div>
            
            <div>
              <p>
                The European Commission, Research<br/>
                Federal Ministry of Education and Research (BMBF)<br/>
                Deutsche Forschungsgemeinschaft (DFG)<br/>
                International Ocean Discovery Program (IODP)
              </p>
            </div>

            <div class="headline underlined">
              Citation
            </div>

            <div>
              <p>
                <strong>Felden, J; Möller, L; Schindler, U; Huber, R; Schumacher, S; Koppe, R; Diepenbroek, M; Glöckner, FO (2023):</strong>
                PANGAEA &ndash; Data Publisher for Earth &amp; Environmental Science. <em>Scientific Data</em>, <strong>10(1)</strong>, 347,
                <a class="text-linkwrap doi-link" href="https://doi.org/10.1038/s41597-023-02269-x" target="_blank">https://doi.org/10.1038/s41597-023-02269-x</a>
              </p>
            </div>
          </div>

          <div class="col-lg-12 col-md-24 col-sm-24 col-xs-24">
            <div class="headline underlined">
              PANGAEA is certified by
            </div>
            
            <div>
              <a href="//www.worlddatasystem.org/" target="_blank" title="World Data System">
                <img class="col-lg-6 col-md-6 col-sm-6 col-xs-6" src="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/logos/logo-wds-block.png" alt="World Data System">
              </a>
              <a href="//www.wmo.int/" target="_blank" title="World Meteorological Organization">
                <img class="col-lg-6 col-md-6 col-sm-6 col-xs-6" src="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/logos/logo-wmo-block.png" alt="World Meteorological Organization">
              </a>
              <a href="//www.coretrustseal.org/" target="_blank" title="CoreTrustSeal">
                <img class="col-lg-6 col-md-6 col-sm-6 col-xs-6" src="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/logos/logo-coretrustseal-block.png" alt="CoreTrustSeal">
              </a>
            </div>
          </div>
        </div>
        <div id="footer-social-area" class="col-lg-3 col-md-24 col-sm-24 col-xs-24">
          <div id="footer-social-area-wrapper" class="col-lg-24 col-md-24 col-sm-24 col-xs-24">
            <div class="blindspalte col-lg-0 col-md-4"></div>
            <div class="col-lg-24 col-md-5 col-md-5 col-xs-10">
              <div class="underlined">Share on...</div>
              <div class="social-icons">
                <a rel="nofollow" class="self-referer-link share-link" href="//www.pangaea.de/nojs.php" data-template="https://www.facebook.com/sharer.php?u=#u#&amp;t=#t#" title="Share on Facebook" target="_blank">
                  <img id="facebook-icon" class="col-lg-12 col-md-12 col-sm-12 col-xs-12" src="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/social-icons/facebook-icon.png" alt="Facebook Icon">
                </a>
                <a rel="nofollow" class="self-referer-link share-link" href="//www.pangaea.de/nojs.php" data-template="https://twitter.com/intent/tweet?url=#u#&amp;text=#t#&amp;via=PANGAEAdataPubl" title="Share on Twitter" target="_blank">
                  <img id="twitter-icon" class="col-lg-12 col-md-12 col-sm-12 col-xs-12" src="//www.pangaea.de/assets/v.bc6abaad9f1b2f791d365aa5c0695d5e/social-icons/twitter-icon.png" alt="Twitter Icon">
                </a>
              </div>
            </div>
            <div class="blindspalte col-lg-0 col-md-18"></div>
          </div>
        </div>
                
        <div id="footer-menu-area" class="col-lg-24 col-md-24 col-sm-24 col-xs-24">
          <div class="blindspalte col-lg-3 col-md-4 col-sm-4 col-xs-4"></div>
          <div id="footer-menu-wrapper" class="col-lg-21 col-md-20 col-sm-24 col-xs-24">
            <nav id="footer-nav">
              <ul>
                <li id="about-legal-notice">
                  <a href="//www.pangaea.de/about/legal.php">Legal notice</a>
                </li>
                <li id="about-term">
                  <a href="//www.pangaea.de/about/terms.php">Terms of use</a>
                </li>
                <li id="about-privacy-policy">
                  <a href="//www.pangaea.de/about/privacypolicy.php">Privacy policy</a>
                </li>
                <li id="about-cookies">
                  <a href="//www.pangaea.de/about/cookies.php">Cookies</a>
                </li>
                <li id="about-jobs">
                  <a href="//www.pangaea.de/about/jobs.php">Jobs</a>
                </li>
                <li id="about-contact">
                  <a href="//www.pangaea.de/contact/">Contact</a>
                </li>
              </ul>
            </nav>
            <div class="clearfix"></div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</div>
</body>
</html>
"""  # noqa 402

decoded_html_body_sample = """"
'\n\n\n<!DOCTYPE html>\n
<html lang="en" dir="ltr">
   \n  
   <head>
   </head>
   \n\n  <body data-invenio-config=\'{"isMathJaxEnabled": "//cdnjs.cloudflare.com/ajax
   /libs/mathjax/3.2.2/es5/tex-mml-chtml.js?config=TeX-AMS-MML_HTMLorMML"}\'  itemscope
     itemtype="http://schema.org/WebPage" data-spy="scroll" data-target=".scrollspy-ta
     rget">\n      <a id="skip-to-main" class="ui button primary ml-5 mt-5 skip-link" 
     href="#main">Skip to main</a>\n      <!--[if lt IE 8]>\n        
   <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please
     <a href="http://browsehappy.com/">upgrade your browser</a> to improve your 
     experience.</p>
   \n      <![endif]-->\n    \n\n
   <div>
      \n  
      <header class="theme header">
         \n\n    
         <div class="outer-navbar">
            \n      
            <div class="ui container invenio-header-container">
               \n        
               <nav id="invenio-nav" class="ui inverted menu borderless p-0">
                  \n          
                  <div class="item logo p-0">\n                    
                  <a class="logo-link" href="/">\n                      
                  <img class="ui image rdm-logo"\n                            
                  src="/static/images/invenio-rdm.svg"\n                            
                  alt="Zenodo home"/>\n                    </a>\n          
                  </div>
                  \n\n          
                  <div id="rdm-burger-toggle">\n            <button\n              
                  id="rdm-burger-menu-icon"\n              
                  class="ui button transparent"\n              
                  aria-label="Menu"\n              aria-haspopup="menu"\n              
                  aria-expanded="false"\n              aria-controls="invenio-menu"\n 
                                        >\n              <span class="navicon" 
                                        aria-hidden="true"></span>\n            
                                        </button>\n          </div>
                  \n\n          <nav\n            id="invenio-menu"\n            
                  aria-labelledby="rdm-burger-menu-icon"\n            
                  class="ui fluid menu borderless mobile-hidden"\n          
                  >\n            <button\n              
                  id="rdm-close-burger-menu-icon"\n              
                  class="ui button transparent"\n              
                  aria-label="Close menu"\n            >\n              
                  <span class="navicon" aria-hidden="true"></span>\n            
                  </button>\n    \n    \n    \n      
                  <div class="item p-0 search-bar">
                     \n        <div id="header-search-bar" data-options=\'[{"key": 
                     "records", "text": "All Zenodo", "value": "/search"}]\'>\n          
                     <div class="ui fluid search">
                        \n            
                        <div class="ui icon input">\n              <input\n
                                                        autocomplete="off"\n           
                                                                  aria-label="Search 
                                                                  records"\n  
                          placeholder="Search records..."\n                
                          type="text"\n                tabindex="0"\n                
                          class="prompt"\n                value=""\n              
                          >\n              <i aria-hidden="true" class="search 
                          icon"></i>\n            </div>
                        \n          
                     </div>
                     \n        
                  </div>
                  \n      
            </div>
         </div>
         \n    
   </div>
   \n      \n      \n    \n      \n    \n    \n      \n        <div class="ui info 
   message top attached m-0 inv-banner" id="banner-78">\n          <div class="ui 
   container">\n              <p><strong>Planned intervention</strong>: On Wednesday,
     October 15th, 06:00 UTC, Zenodo will be unavailable for 1-2 minutes to perform a 
     storage cluster upgrade.</p>\n          </div>\n        </div>\n      \n    \n  
     </header>\n</div>\n\n  
   <main id="main">
      \n    
      <div class="invenio-page-body">
         \n  
         <section id="banners" class="banners" aria-label="Information banner">
            \n    <!-- COMMUNITY HEADER: hide it when displaying the submission 
            request -->\n    \n      \n    \n    <!-- /COMMUNITY HEADER -->\n\n    
            <!-- PREVIEW HEADER -->\n    \n    <!-- /PREVIEW HEADER -->\n\n    \n  
         </section>
         \n\n\n  
         <div class="ui container">
            \n    
            <div class="ui relaxed grid mt-5">
            </div>
            \n  
            \n\n    </section>\n              \n\n  
            <section id="additional-details" class="rel-mt-2" aria-label="Additional 
            record details">\n\n\n\n\n\n\n\n\n\n\n\n\n\n  \n\n  </section>
            \n    \n    <section\n      id="citations-search"\n      
            data-record-pids=\'{"doi": {"client": "datacite", "identifier": 
            "10.5281/zenodo.8255910", "provider": "datacite"}, "oai": {"identifier": 
            "oai:zenodo.org:8255910", "provider": "oai"}}\'\n      
            data-record-parent-pids=\'{"doi": {"client": "datacite", "identifier": 
            "10.5281/zenodo.8255909", "provider": "datacite"}}\'\n      
            data-citations-endpoint="https://zenodo-broker.web.cern.ch/api/
            relationships"\n      aria-label="Record citations"\n      class="rel-mb-1"
            \n    >\n    </section>\n  \n        </article>\n\n        \n        
            <aside class="sixteen wide tablet five wide computer column sidebar"\n
                                          aria-label="Record details">
               \n          \n\n\n\n\n
               <div class="sidebar-container">
                  \n  
                  <h2 class="ui medium top attached header mt-0">Versions</h2>
                  \n  
                  <div id="record-versions" class="ui segment rdm-sidebar bottom 
                  attached pl-0 pr-0 pt-0">
                     \n    
                     <div class="versions">
                        \n      <div id="recordVersions" data-record=\'{"access": 
                        {"embargo": {"active": false, "reason": null}, "files": 
                        "public", "record": "public", "status": "open"}, "created": 
                        "2023-08-17T11:20:32.047273+00:00", "custom_fields": {}, 
                        "deletion_status": {"is_deleted": false, "status": "P"}, 
                        "expanded": {"parent": {"access": {"owned_by": 
                        {"active": null, "blocked_at": null, "confirmed_at": null, 
                        "email": "", "id": "587568", "is_current_user": false, 
                        "links": {"avatar": 
                        "https://zenodo.org/api/users/587568/avatar.svg", 
                        "records_html": 
                        "https://zenodo.org/search/records?q=parent.access.owned_by.user:587568", "self": "https://zenodo.org/api/users/587568"}, "profile": {"affiliations": "", "full_name": ""}, "username": "eduardosoares", "verified_at": null}}}}, "files": {"count": 8, "enabled": true, "entries": {"All-Public_dataset_Mordred.csv": {"access": {"hidden": false}, "checksum": "md5:a4b8e6e9149ad7f3a3ce346e3a627bac", "ext": "csv", "id": "5b239a2c-29ca-4885-9ecc-b755e427cacb", "key": "All-Public_dataset_Mordred.csv", "links": {"content": "https://zenodo.org/api/records/8255910/files/All-Public_dataset_Mordred.csv/content", "self": "https://zenodo.org/api/records/8255910/files/All-Public_dataset_Mordred.csv"}, "metadata": null, "mimetype": "text/csv", "size": 53040614, "storage_class": "L"}, "ECHA_biodegradability_compounds.csv": {"access": {"hidden": false}, "checksum": "md5:6e4cafe74f5c8719273c926813f9dbcb", "ext": "csv", "id": "4b647d94-671d-44b5-97b8-9a13ca15184a", "key": "ECHA_biodegradability_compounds.csv", "links": {"content": "https://zenodo.org/api/records/8255910/files/ECHA_biodegradability_compounds.csv/content", "self": "https://zenodo.org/api/records/8255910/files/ECHA_biodegradability_compounds.csv"}, "metadata": null, "mimetype": "text/csv", "size": 2501709, "storage_class": "L"}, "ECHA_biodegradability_new_compounds.csv": {"access": {"hidden": false}, "checksum": "md5:9ed2ab5d82fbf5671a948b50f41606f5", "ext": "csv", "id": "89bc955e-1376-4a55-bae0-f52d80cf482e", "key": "ECHA_biodegradability_new_compounds.csv", "links": {"content": "https://zenodo.org/api/records/8255910/files/ECHA_biodegradability_new_compounds.csv/content", "self": "https://zenodo.org/api/records/8255910/files/ECHA_biodegradability_new_compounds.csv"}, "metadata": null, "mimetype": "text/csv", "size": 1999408, "storage_class": "L"}, "ECHA_raw_NRB_compounds.csv": {"access": {"hidden": false}, "checksum": "md5:79609893de1fc6a83847fe9ad1d39633", "ext": "csv", "id": "b07c033a-c1c6-450e-8cc9-ba65231da6e6", "key": "ECHA_raw_NRB_compounds.csv", "links": {"content": "https://zenodo.org/api/records/8255910/files/ECHA_raw_NRB_compounds.csv/content", "self": "https://zenodo.org/api/records/8255910/files/ECHA_raw_NRB_compounds.csv"}, "metadata": null, "mimetype": "text/csv", "size": 3129240, "storage_class": "L"}, "ECHA_raw_RB_compounds.csv": {"access": {"hidden": false}, "checksum": "md5:81f6961dcd00d572aa04552cc0796533", "ext": "csv", "id": "2038cfbc-4ab0-4fff-b1b4-e3bab8bad6c5", "key": "ECHA_raw_RB_compounds.csv", "links": {"content": "https://zenodo.org/api/records/8255910/files/ECHA_raw_RB_compounds.csv/content", "self": "https://zenodo.org/api/records/8255910/files/ECHA_raw_RB_compounds.csv"}, "metadata": null, "mimetype": "text/csv", "size": 6344039, "storage_class": "L"}, "ECHA_results_NRB_compounds.csv": {"access": {"hidden": false}, "checksum": "md5:d7f7d446e50e5b5e2ed6d515a51b04bd", "ext": "csv", "id": "b923fa6c-957f-41b8-9231-611d07db61c0", "key": "ECHA_results_NRB_compounds.csv", "links": {"content": "https://zenodo.org/api/records/8255910/files/ECHA_results_NRB_compounds.csv/content", "self": "https://zenodo.org/api/records/8255910/files/ECHA_results_NRB_compounds.csv"}, "metadata": null, "mimetype": "text/csv", "size": 1410455, "storage_class": "L"}, "ECHA_results_RB_compounds.csv": {"access": {"hidden": false}, "checksum": "md5:30a2b07a9da3967945b4ccf6cefebbc5", "ext": "csv", "id": "06a59d2e-2e12-453c-9aa1-0c537098480f", "key": "ECHA_results_RB_compounds.csv", "links": {"content": "https://zenodo.org/api/records/8255910/files/ECHA_results_RB_compounds.csv/content", "self": "https://zenodo.org/api/records/8255910/files/ECHA_results_RB_compounds.csv"}, "metadata": null, "mimetype": "text/csv", "size": 1981857, "storage_class": "L"}, "Expanded_Biodegradability_Dataset.ipynb": {"access": {"hidden": false}, "checksum": "md5:c179f26f9d4a233dbed7760449c8f093", "ext": "bin", "id": "0b7412f2-fcd4-4da9-8434-a3994f077b88", "key": "Expanded_Biodegradability_Dataset.ipynb", "links": {"content": "https://zenodo.org/api/records/8255910/files/Expanded_Biodegradability_Dataset.ipynb/content", "self": "https://zenodo.org/api/records/8255910/files/Expanded_Biodegradability_Dataset.ipynb"}, "metadata": null, "mimetype": "application/octet-stream", "size": 61066, "storage_class": "L"}}, "order": [], "total_bytes": 70468388}, "id": "8255910", "is_draft": false, "is_published": true, "links": {"access": "https://zenodo.org/api/records/8255910/access", "access_grants": "https://zenodo.org/api/records/8255910/access/grants", "access_links": "https://zenodo.org/api/records/8255910/access/links", "access_request": "https://zenodo.org/api/records/8255910/access/request", "access_users": "https://zenodo.org/api/records/8255910/access/users", "archive": "https://zenodo.org/api/records/8255910/files-archive", "archive_media": "https://zenodo.org/api/records/8255910/media-files-archive", "communities": "https://zenodo.org/api/records/8255910/communities", "communities-suggestions": "https://zenodo.org/api/records/8255910/communities-suggestions", "doi": "https://doi.org/10.5281/zenodo.8255910", "draft": "https://zenodo.org/api/records/8255910/draft", "files": "https://zenodo.org/api/records/8255910/files", "latest": "https://zenodo.org/api/records/8255910/versions/latest", "latest_html": "https://zenodo.org/records/8255910/latest", "media_files": "https://zenodo.org/api/records/8255910/media-files", "parent": "https://zenodo.org/api/records/8255909", "parent_doi": "https://doi.org/10.5281/zenodo.8255909", "parent_doi_html": "https://zenodo.org/doi/10.5281/zenodo.8255909", "parent_html": "https://zenodo.org/records/8255909", "preview_html": "https://zenodo.org/records/8255910?preview=1", "request_deletion": "https://zenodo.org/api/records/8255910/request-deletion", "requests": "https://zenodo.org/api/records/8255910/requests", "reserve_doi": "https://zenodo.org/api/records/8255910/draft/pids/doi", "self": "https://zenodo.org/api/records/8255910", "self_doi": "https://doi.org/10.5281/zenodo.8255910", "self_doi_html": "https://zenodo.org/doi/10.5281/zenodo.8255910", "self_html": "https://zenodo.org/records/8255910", "self_iiif_manifest": "https://zenodo.org/api/iiif/record:8255910/manifest", "self_iiif_sequence": "https://zenodo.org/api/iiif/record:8255910/sequence/default", "versions": "https://zenodo.org/api/records/8255910/versions"}, "media_files": {"count": 0, "enabled": false, "entries": {}, "order": [], "total_bytes": 0}, "metadata": {"additional_descriptions": [{"description": "Published at the ACS Fall 2023", "type": {"id": "notes", "title": {"de": "Anmerkungen", "en": "Notes"}}}], "creators": [{"affiliations": [{"name": "IBM"}], "person_or_org": {"family_name": "Eduardo Almeida Soares", "identifiers": [{"identifier": "0000-0002-2634-8270", "scheme": "orcid"}], "name": "Eduardo Almeida Soares", "type": "personal"}}, {"affiliations": [{"name": "IBM"}], "person_or_org": {"family_name": "Victor Shirasuna", "name": "Victor Shirasuna", "type": "personal"}}, {"affiliations": [{"name": "IBM"}], "person_or_org": {"family_name": "Emilio Vital Brazil", "name": "Emilio Vital Brazil", "type": "personal"}}], "description": "\\u003cp\\u003eBiodegradability is a crucial factor in assessing the long-term impact of chemicals on the environment. However, experimental testing to determine biodegradability is time-consuming and laborious. To address this issue, \\u003cem\\u003ein silico \\u003c/em\\u003eapproaches such as quantitative structure-activity relationship (QSAR) models are highly encouraged by legislators.\\u003c/p\\u003e\\n\\n\\u003cp\\u003e\\u0026nbsp;\\u003c/p\\u003e\\n\\n\\u003cp\\u003eEuropean legislators have incorporated chemical persistency in the Registration, Evaluation, and Authorization of Chemicals (REACH) for the assessment of chemicals. However, only 61% of chemicals produced or imported in quantities of over 1000 tons per year have information on biodegradability. As a potential solution, REACH encourages the use of QSAR models to predict the biodegradability of compounds.\\u003c/p\\u003e\\n\\n\\u003cp\\u003e\\u0026nbsp;\\u003c/p\\u003e\\n\\n\\u003cp\\u003eTo encourage the development of QSAR models to predict the biodegradability of compounds, this work extends the \\u0026quot;All-Public set,\\u0026quot; which is an aggregated dataset with information on 2830 compounds from various sources. In this study, we contribute to this dataset by adding information on the biodegradability of 3707 new compounds from the ECHA database, resulting in a larger dataset with the biodegradability information of 6537 compounds.\\u003c/p\\u003e\\n\\n\\u003cp\\u003e\\u0026nbsp;\\u003c/p\\u003e\\n\\n\\u003cp\\u003eBy providing a larger dataset with biodegradability information, we aim to promote the development of more accurate QSAR models for predicting the biodegradability of compounds. This will enable more efficient and effective assessments of the potential impact of chemicals on the environment, facilitating the development of more sustainable and environmentally friendly products.\\u003c/p\\u003e", "publication_date": "2023-08-17", "publisher": "Zenodo", "resource_type": {"id": "dataset", "title": {"de": "Datensatz", "en": "Dataset"}}, "rights": [{"description": {"en": "The Creative Commons Attribution license allows re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited."}, "icon": "cc-by-icon", "id": "cc-by-4.0", "props": {"scheme": "spdx", "url": "https://creativecommons.org/licenses/by/4.0/legalcode"}, "title": {"en": "Creative Commons Attribution 4.0 International"}}], "subjects": [{"subject": "Biodegradability"}, {"subject": "QSAR"}, {"subject": "dataset"}, {"subject": "Machine Learning"}], "title": "An Expanded Dataset for Improved Prediction of Chemical Biodegradability", "version": "1.0"}, "parent": {"access": {"owned_by": {"user": "587568"}, "settings": {"accept_conditions_text": null, "allow_guest_requests": false, "allow_user_requests": false, "secret_link_expiration": 0}}, "communities": {}, "id": "8255909", "pids": {"doi": {"client": "datacite", "identifier": "10.5281/zenodo.8255909", "provider": "datacite"}}}, "pids": {"doi": {"client": "datacite", "identifier": "10.5281/zenodo.8255910", "provider": "datacite"}, "oai": {"identifier": "oai:zenodo.org:8255910", "provider": "oai"}}, "revision_id": 5, "stats": {"all_versions": {"data_volume": 41024021855.0, "downloads": 3614, "unique_downloads": 1680, "unique_views": 426, "views": 519}, "this_version": {"data_volume": 40794431625.0, "downloads": 3603, "unique_downloads": 1677, "unique_views": 423, "views": 516}}, "status": "published", "swh": {}, "ui": {"access_status": {"description_l10n": "The record and files are publicly accessible.", "embargo_date_l10n": null, "icon": "unlock", "id": "open", "message_class": "", "title_l10n": "Open"}, "additional_descriptions": [{"description": "Published at the ACS Fall 2023", "type": {"id": "notes", "title_l10n": "Notes"}}], "created_date_l10n_long": "August 17, 2023", "creators": {"affiliations": [[1, "IBM", null]], "creators": [{"affiliations": [[1, "IBM"]], "person_or_org": {"family_name": "Eduardo Almeida Soares", "identifiers": [{"identifier": "0000-0002-2634-8270", "scheme": "orcid"}], "name": "Eduardo Almeida Soares", "type": "personal"}}, {"affiliations": [[1, "IBM"]], "person_or_org": {"family_name": "Victor Shirasuna", "name": "Victor Shirasuna", "type": "personal"}}, {"affiliations": [[1, "IBM"]], "person_or_org": {"family_name": "Emilio Vital Brazil", "name": "Emilio Vital Brazil", "type": "personal"}}]}, "custom_fields": {}, "description_stripped": "Biodegradability is a crucial factor in assessing the long-term impact of chemicals on the environment. However, experimental testing to determine biodegradability is time-consuming and laborious. To address this issue, in silico approaches such as quantitative structure-activity relationship (QSAR) models are highly encouraged by legislators.\\n\\n\\n\\u00a0\\n\\n\\nEuropean legislators have incorporated chemical persistency in the Registration, Evaluation, and Authorization of Chemicals (REACH) for the assessment of chemicals. However, only 61% of chemicals produced or imported in quantities of over 1000 tons per year have information on biodegradability. As a potential solution, REACH encourages the use of QSAR models to predict the biodegradability of compounds.\\n\\n\\n\\u00a0\\n\\n\\nTo encourage the development of QSAR models to predict the biodegradability of compounds, this work extends the \\"All-Public set,\\" which is an aggregated dataset with information on 2830 compounds from various sources. In this study, we contribute to this dataset by adding information on the biodegradability of 3707 new compounds from the ECHA database, resulting in a larger dataset with the biodegradability information of 6537 compounds.\\n\\n\\n\\u00a0\\n\\n\\nBy providing a larger dataset with biodegradability information, we aim to promote the development of more accurate QSAR models for predicting the biodegradability of compounds. This will enable more efficient and effective assessments of the potential impact of chemicals on the environment, facilitating the development of more sustainable and environmentally friendly products.", "is_draft": false, "publication_date_l10n_long": "August 17, 2023", "publication_date_l10n_medium": "Aug 17, 2023", "resource_type": {"id": "dataset", "title_l10n": "Dataset"}, "rights": [{"description_l10n": "The Creative Commons Attribution license allows re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited.", "icon": "cc-by-icon", "id": "cc-by-4.0", "props": {"scheme": "spdx", "url": "https://creativecommons.org/licenses/by/4.0/legalcode"}, "title_l10n": "Creative Commons Attribution 4.0 International"}], "updated_date_l10n_long": "July 23, 2025", "version": "1.0"}, "updated": "2025-07-23T17:22:42.236301+00:00", "versions": {"index": 1, "is_latest": true}}\' data-preview=\'false\'>\n        
                        <div class="rel-p-1"></div>
                        \n        
                        <div class="ui fluid placeholder rel-mr-1 rel-ml-1"></div>
                        \n        
                        <div class="header">
                           \n          
                           <div class="line"></div>
                           \n          
                           <div class="line"></div>
                           \n          
                           <div class="line"></div>
                           \n        
                        </div>
                        \n      
                     </div>
                     \n    
                  </div>
                  \n  
               </div>
               \n
         </div>
         </div>
        <div class="ui container">
         \n      
         <div class="ui relaxed grid">
            \n        
            <div class="two column row">
               \n          
               <div class="sixteen wide tablet eleven wide computer column">
                  \n            
                  <div class="ui grid">
                     \n                
                     <div class="centered row rel-mt-1">\n                  <button id="jump-btn" class="jump-to-top ui button labeled icon"\n                          aria-label="Jump to top of page">\n                    <i class="arrow alternate circle up outline icon"></i>\n                    Jump up\n                  </button>\n                </div>
                     \n              
                  </div>
               </div>
               \n        
            </div>
            \n      
         </div>
         \n    
      </div>
      \n  </div>\n    </div>\n  
   </main>
   \n
      <div class="ui container info message cookie-banner hidden">
      \n  <i class="close icon"></i>\n  
      <div>
         \n    <i aria-hidden="true" class="info icon"></i>\n    
         <p class="inline">This site uses cookies. Find out more on <a href="https://about.zenodo.org/cookie-policy">how we use cookies</a></p>
         \n  
      </div>
      \n  
      <div class="buttons">\n    <button class="ui button small primary" id="cookies-all">Accept all cookies</button>\n    <button class="ui button small" id="cookies-essential">Accept only essential cookies</button>\n  </div>
      \n
   </div>
</html>
'
"""  # noqa: W291, E501
