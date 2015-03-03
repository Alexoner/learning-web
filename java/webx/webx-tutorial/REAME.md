[webx official website]:http://openwebx.org/

webx URL route rules:

Example file system:
├── all
│   └── pom.xml
├── biz
│   ├── common
│   │   ├── pom.xml
│   │   ├── src
│   │   │   ├── main
│   │   │   │   ├── java
│   │   │   │   │   └── com
│   │   │   │   │       └── company
│   │   │   │   │           └── mirror
│   │   │   │   │               └── biz
│   │   │   │   │                   └── common
│   │   │   │   │                       ├── dao
│   │   │   │   │                       │   ├── GeneralDao.java
│   │   │   │   │                       │   └── impl
│   │   │   │   │                       │       └── GeneralDaoImpl.java
│   │   │   │   │                       └── exception
│   │   │   │   │                           ├── DaoException.java
│   │   │   │   │                           └── myprojException.java
│   │   │   │   └── resources
│   │   │   │       └── META-INF
│   │   │   │           ├── autoconfig
│   │   │   │           │   ├── auto-config.xml
│   │   │   │           │   └── sys.properties
│   │   │   │           └── common
│   │   │   │               ├── beans
│   │   │   │               │   ├── alimonitor.xml
│   │   │   │               │   ├── service-config.xml
│   │   │   │               │   ├── sys-properties.xml
│   │   │   │               │   └── tddl-config.xml
│   │   │   │               └── properties
│   │   │   └── test
│   │   │       └── java
│   │   └── target
│   │       ├── classes
│   │       │   ├── com
│   │       │   │   └── company
│   │       │   │       └── mirror
│   │       │   │           └── biz
│   │       │   │               └── common
│   │       │   │                   ├── dao
│   │       │   │                   │   ├── GeneralDao.class
│   │       │   │                   │   └── impl
│   │       │   │                   │       └── GeneralDaoImpl.class
│   │       │   │                   └── exception
│   │       │   │                       ├── DaoException.class
│   │       │   │                       └── myprojException.class
│   │       │   └── META-INF
│   │       │       ├── autoconfig
│   │       │       │   ├── auto-config.xml
│   │       │       │   ├── auto-config.xml.log
│   │       │       │   └── sys.properties
│   │       │       └── common
│   │       │           ├── beans
│   │       │           │   ├── alimonitor.xml
│   │       │           │   ├── service-config.xml
│   │       │           │   ├── sys-properties.xml
│   │       │           │   └── tddl-config.xml
│   │       │           └── properties
│   │       │               └── sys.properties
│   │       ├── maven-archiver
│   │       │   └── pom.properties
│   │       ├── myproj_biz.common-1.0-SNAPSHOT.jar
│   │       ├── myproj_biz.common-1.0-SNAPSHOT-sources.jar
│   │       └── test-classes
│   └── competitor
│       ├── pom.xml
│       ├── src
│       │   ├── main
│       │   │   ├── java
│       │   │   │   └── com
│       │   │   │       └── company
│       │   │   │           └── myproj
│       │   │   │               └── biz
│       │   │   │                   └── competitor
│       │   │   │                       ├── dao
│       │   │   │                       └── service
│       │   │   │                           ├── impl
│       │   │   │                           │   ├── InnerBrandServiceImpl.java
│       │   │   │                           │   └── MockInnerBrandServiceImpl.java
│       │   │   │                           └── InnerBrandService.java
│       │   │   └── resources
│       │   │       └── META-INF
│       │   │           ├── autoconfig
│       │   │           │   ├── auto-config.xml
│       │   │           │   └── sys.properties
│       │   │           └── competitor
│       │   │               ├── beans
│       │   │               │   └── service-config.xml
│       │   │               ├── ibatis
│       │   │               └── properties
│       │   └── test
│       │       └── java
│       └── target
│           ├── classes
│           │   ├── com
│           │   │   └── company
│           │   │       └── myproj
│           │   │           └── biz
│           │   │               └── competitor
│           │   │                   ├── dao
│           │   │                   └── service
│           │   │                       ├── impl
│           │   │                       │   ├── InnerBrandServiceImpl.class
│           │   │                       │   └── MockInnerBrandServiceImpl.class
│           │   │                       └── InnerBrandService.class
│           │   └── META-INF
│           │       ├── autoconfig
│           │       │   ├── auto-config.xml
│           │       │   ├── auto-config.xml.log
│           │       │   └── sys.properties
│           │       └── competitor
│           │           ├── beans
│           │           │   └── service-config.xml
│           │           └── properties
│           │               └── sys.properties
│           ├── maven-archiver
│           │   └── pom.properties
│           ├── myproj_biz.competitor-1.0-SNAPSHOT.jar
│           ├── myproj_biz.competitor-1.0-SNAPSHOT-sources.jar
│           └── test-classes
├── bundle
│   └── war
│       ├── antx.properties
│       ├── logs
│       ├── pom.xml
│       ├── src
│       │   └── main
│       │       └── webapp
│       │           ├── common
│       │           │   ├── htdocs
│       │           │   └── templates
│       │           │       ├── macros.vm
│       │           │       └── screen
│       │           │           ├── error.vm
│       │           │           ├── index.vm
│       │           │           └── ok.vm
│       │           ├── competitor
│       │           │   └── templates
│       │           │       ├── control
│       │           │       ├── layout
│       │           │       └── screen
│       │           │           └── index.vm
│       │           ├── error.jsp
│       │           ├── META-INF
│       │           │   └── autoconf
│       │           │       ├── auto-config.xml
│       │           │       ├── log4j.xml.vm
│       │           │       └── web.xml.vm
│       │           ├── ok.jsp
│       │           └── WEB-INF
│       │               ├── framework
│       │               │   ├── form.xml
│       │               │   ├── pipeline-exception.xml
│       │               │   ├── pipeline.xml
│       │               │   ├── resources.xml
│       │               │   ├── uris.xml
│       │               │   ├── webx-component-and-root.xml
│       │               │   └── webx-component.xml
│       │               ├── jboss-web.xml
│       │               ├── webx-common.xml
│       │               ├── webx-competitor.xml
│       │               ├── web.xml
│       │               └── webx.xml
│       └── target
│           ├── classes
│           ├── m2e-wtp
│           │   └── web-resources
│           │       └── META-INF
│           │           ├── MANIFEST.MF
│           │           └── maven
│           │               └── com.company.myproj
│           │                   └── myproj_bundle.war
│           │                       ├── pom.properties
│           │                       └── pom.xml
│           ├── maven-archiver
│           │   └── pom.properties
│           ├── myproj_bundle.war-1.0-SNAPSHOT
│           │   ├── common
│           │   │   └── templates
│           │   │       ├── macros.vm
│           │   │       └── screen
│           │   │           ├── error.vm
│           │   │           ├── index.vm
│           │   │           └── ok.vm
│           │   ├── competitor
│           │   │   └── templates
│           │   │       └── screen
│           │   │           └── index.vm
│           │   ├── error.jsp
│           │   ├── META-INF
│           │   │   └── autoconf
│           │   │       ├── auto-config.xml
│           │   │       ├── log4j.xml.vm
│           │   │       └── web.xml.vm
│           │   ├── ok.jsp
│           │   └── WEB-INF
│           │       ├── classes
│           │       ├── framework
│           │       │   ├── form.xml
│           │       │   ├── pipeline-exception.xml
│           │       │   ├── pipeline.xml
│           │       │   ├── resources.xml
│           │       │   ├── uris.xml
│           │       │   ├── webx-component-and-root.xml
│           │       │   └── webx-component.xml
│           │       ├── jboss-web.xml
│           │       ├── lib
│           │       │   ├── alimonitor-jmonitor-1.0.4.jar
│           │       │   ├── ant-launcher-1.7.1.jar
│           │       │   ├── aopalliance-1.0.jar
│           │       │   ├── asm-1.5.3.jar
│           │       │   ├── asm-attrs-1.5.3.jar
│           │       │   ├── aspectjrt-1.5.4.jar
│           │       │   ├── aspectjweaver-1.5.4.jar
│           │       │   ├── batik-css-1.7.jar
│           │       │   ├── batik-ext-1.6-1.jar
│           │       │   ├── batik-ext-1.7.jar
│           │       │   ├── batik-gui-util-1.6-1.jar
│           │       │   ├── batik-util-1.6-1.jar
│           │       │   ├── batik-util-1.7.jar
│           │       │   ├── buc.legacy-0.0.1.jar
│           │       │   ├── buc.sso.api-0.6.3.jar
│           │       │   ├── buc.sso.client-0.6.3.jar
│           │       │   ├── buc.sso.common-0.6.3.jar
│           │       │   ├── buc.uc.api-0.7.38.jar
│           │       │   ├── cglib-99.0-does-not-exist.jar
│           │       │   ├── cglib-nodep-2.2.jar
│           │       │   ├── citrus-webx-all-3.0.7.jar
│           │       │   ├── codehaus.groovy-1.6.3.jar
│           │       │   ├── commons-codec-1.3.jar
│           │       │   ├── commons-collections-3.2.1.jar
│           │       │   ├── commons-fileupload-1.2.1.jar
│           │       │   ├── commons-io-1.4.jar
│           │       │   ├── commons-jexl-1.1.jar
│           │       │   ├── commons-jexl-2.0.1.jar
│           │       │   ├── commons-lang-2.6.jar
│           │       │   ├── commons-logging-99.0-does-not-exist.jar
│           │       │   ├── diamond-client-3.6.8.jar
│           │       │   ├── diamond-utils-3.1.4.jar
│           │       │   ├── dom4j-1.6.1.jar
│           │       │   ├── druid-1.0.12.jar
│           │       │   ├── eagleeye-core-1.3.1.jar
│           │       │   ├── ecs-1.4.2.jar
│           │       │   ├── fastjson-1.1.2.jar
│           │       │   ├── fastjson-1.1.30.jar
│           │       │   ├── fasttext.all-1.3-20150112.071739-59.jar
│           │       │   ├── fasttext-css-1.3.51.jar
│           │       │   ├── fasttext-html-1.3.51.jar
│           │       │   ├── fasttext-psoriasis-1.3.51.jar
│           │       │   ├── fasttext-sec-1.3.51.jar
│           │       │   ├── fasttext-segment-1.3.51.jar
│           │       │   ├── fasttext-utils-1.3.51.jar
│           │       │   ├── freemarker-2.3.16.jar
│           │       │   ├── fulllinkstresstesting-0.9.2.jar
│           │       │   ├── groovy-all-1.6.3.jar
│           │       │   ├── guava-15.0.jar
│           │       │   ├── hamcrest-core-1.3.jar
│           │       │   ├── htmlparser-1.6.jar
│           │       │   ├── ibatis2-sqlmap-2.3.4.726-patch.jar
│           │       │   ├── icu4j-2.6.1.jar
│           │       │   ├── jackson-core-lgpl-1.9.6.jar
│           │       │   ├── jackson-mapper-lgpl-1.9.6.jar
│           │       │   ├── jakarta.ant-1.7.1.jar
│           │       │   ├── jakarta.ant.launcher-1.7.1.jar
│           │       │   ├── jakarta.commons.codec-1.3.jar
│           │       │   ├── jakarta.commons.collections-3.2.1.jar
│           │       │   ├── jakarta.commons.io-1.4.jar
│           │       │   ├── jakarta.commons.jexl-1.1.jar
│           │       │   ├── jakarta.commons.lang-2.4.jar
│           │       │   ├── jakarta.commons.logging-0.0.0.jar
│           │       │   ├── jakarta.ecs-1.4.2.jar
│           │       │   ├── jakarta.log4j-1.2.8.jar
│           │       │   ├── jakarta.oro-2.0.8.jar
│           │       │   ├── jakarta.velocity-1.6.4.jar
│           │       │   ├── jaxen-1.1.jar
│           │       │   ├── jcl-over-slf4j-1.7.10.jar
│           │       │   ├── jdom-1.0.jar
│           │       │   ├── je-5.0.73.jar
│           │       │   ├── jline-0.9.94.jar
│           │       │   ├── junit-4.11.jar
│           │       │   ├── log4j-1.2.17.jar
│           │       │   ├── myproj_biz.common-1.0-SNAPSHOT.jar
│           │       │   ├── myproj_biz.competitor-1.0-SNAPSHOT.jar
│           │       │   ├── myproj_web.common-1.0-SNAPSHOT.jar
│           │       │   ├── myproj_web.competitor-1.0-SNAPSHOT.jar
│           │       │   ├── mysql-connector-java-5.1.33.jar
│           │       │   ├── nekohtml-1.9.9.jar
│           │       │   ├── objectweb.asm-0.0.0.jar
│           │       │   ├── objectweb.asm.attrs-0.0.0.jar
│           │       │   ├── oro-2.0.8.jar
│           │       │   ├── persistence-api-1.0.2.jar
│           │       │   ├── sac-1.3.jar
│           │       │   ├── servlet-api-2.5.jar
│           │       │   ├── slf4j-api-1.7.10.jar
│           │       │   ├── slf4j-log4j12-1.7.10.jar
│           │       │   ├── sourceforge.freemarker-2.3.15.jar
│           │       │   ├── sourceforge.spring-2.5.6.SEC02.jar
│           │       │   ├── sourceforge.spring.modules.webmvc-2.5.6.SEC02.jar
│           │       │   ├── sourceforge.spring.weaving.aspects-2.5.4.jar
│           │       │   ├── spring-2.5.6.SEC02.jar
│           │       │   ├── spring-aop-2.5.6.SEC03.jar
│           │       │   ├── spring-aspects-2.5.4.jar
│           │       │   ├── spring-beans-2.5.6.SEC03.jar
│           │       │   ├── spring-context-2.5.6.SEC03.jar
│           │       │   ├── spring-context-support-2.5.6.SEC03.jar
│           │       │   ├── spring-core-2.5.6.SEC03.jar
│           │       │   ├── spring-jdbc-2.5.6.SEC03.jar
│           │       │   ├── spring-orm-2.5.6.SEC03.jar
│           │       │   ├── spring-tx-2.5.6.SEC03.jar
│           │       │   ├── spring-web-2.5.6.SEC03.jar
│           │       │   ├── spring-webmvc-2.5.6.SEC03.jar
│           │       │   ├── tddl-atom-5.1.17.jar
│           │       │   ├── tddl-client-5.1.17.jar
│           │       │   ├── tddl-common-5.1.17.jar
│           │       │   ├── tddl-config-5.1.17.jar
│           │       │   ├── tddl-config-diamond-5.1.17.jar
│           │       │   ├── tddl-executor-5.1.17.jar
│           │       │   ├── tddl-group-5.1.17.jar
│           │       │   ├── tddl-matrix-5.1.17.jar
│           │       │   ├── tddl-monitor-5.1.17.jar
│           │       │   ├── tddl-optimizer-5.1.17.jar
│           │       │   ├── tddl-parser-5.1.17.jar
│           │       │   ├── tddl-repo-bdb-5.1.17.jar
│           │       │   ├── tddl-repo-demo-5.1.17.jar
│           │       │   ├── tddl-repo-mysql-5.1.17.jar
│           │       │   ├── tddl-rule-5.1.17.jar
│           │       │   ├── tddl-sequence-5.1.17.jar
│           │       │   ├── unitrouter-1.0.11.jar
│           │       │   ├── velocity-1.6.1-patch.jar
│           │       │   ├── webx3.core-3.0.6.jar
│           │       │   ├── xalan-2.6.0.jar
│           │       │   ├── xercesImpl-2.5.0.jar
│           │       │   ├── xml.apis-0.0.0.jar
│           │       │   ├── xml-apis-1.3.04.jar
│           │       │   ├── xml.apis.css-1.3.jar
│           │       │   ├── xml-apis-ext-1.3.04.jar
│           │       │   ├── xml.commons-resolver-0.0.0.jar
│           │       │   ├── xml.dom4j-1.6.1.jar
│           │       │   ├── xml.nekohtml-1.9.9.jar
│           │       │   ├── xmlParserAPIs-2.6.2.jar
│           │       │   ├── xml-resolver-1.2.jar
│           │       │   ├── xml.xerces-0.0.0.jar
│           │       │   ├── xml.xmlgraphics-1.7.jar
│           │       │   ├── xml.xmlgraphics__batik-css-1.7.jar-1.7.jar
│           │       │   ├── xml.xmlgraphics__batik-util-1.6-1.jar-1.7.jar
│           │       │   └── xom-1.0.jar
│           │       ├── webx-common.xml
│           │       ├── webx-competitor.xml
│           │       ├── web.xml
│           │       └── webx.xml
│           ├── myproj_bundle.war-1.0-SNAPSHOT-sources.jar
│           └── test-classes
├── target
│   └── myproj.war
└── web
    ├── common
    │   ├── pom.xml
    │   ├── src
    │   │   ├── main
    │   │   │   ├── java
    │   │   │   │   └── com
    │   │   │   │       └── company
    │   │   │   │           └── myproj
    │   │   │   │               └── web
    │   │   │   │                   └── common
    │   │   │   │                       ├── module
    │   │   │   │                       │   ├── action
    │   │   │   │                       │   │   └── TemplateAction.java
    │   │   │   │                       │   └── screen
    │   │   │   │                       │       └── Index.java
    │   │   │   │                       └── util
    │   │   │   │                           └── ResponseWriteUtils.java
    │   │   │   └── resources
    │   │   │       └── META-INF
    │   │   └── test
    │   │       └── java
    │   └── target
    │       ├── classes
    │       │   └── com
    │       │       └── company
    │       │           └── myproj
    │       │               └── web
    │       │                   └── common
    │       │                       ├── module
    │       │                       │   ├── action
    │       │                       │   │   └── TemplateAction.class
    │       │                       │   └── screen
    │       │                       │       └── Index.class
    │       │                       └── util
    │       │                           └── ResponseWriteUtils.class
    │       ├── maven-archiver
    │       │   └── pom.properties
    │       ├── myproj_web.common-1.0-SNAPSHOT.jar
    │       ├── myproj_web.common-1.0-SNAPSHOT-sources.jar
    │       └── test-classes
    └── competitor
        ├── pom.xml
        ├── src
        │   ├── main
        │   │   ├── java
        │   │   │   └── com
        │   │   │       └── company
        │   │   │           └── myproj
        │   │   │               └── web
        │   │   │                   └── competitor
        │   │   │                       └── module
        │   │   │                           ├── action
        │   │   │                           │   ├── BrandDataAction.java
        │   │   │                           │   ├── MetaDataAction.java
        │   │   │                           │   ├── ProductDataAction.java
        │   │   │                           │   └── TemplateAction.java
        │   │   │                           └── screen
        │   │   │                               └── Index.java
        │   │   └── resources
        │   │       └── META-INF
        │   └── test
        │       └── java
        └── target
            ├── classes
            │   └── com
            │       └── company
            │           └── myproj
            │               └── web
            │                   └── competitor
            │                       └── module
            │                           ├── action
            │                           │   ├── BrandDataAction.class
            │                           │   ├── MetaDataAction.class
            │                           │   ├── ProductDataAction.class
            │                           │   └── TemplateAction.class
            │                           └── screen
            │                               └── Index.class
            ├── maven-archiver
            │   └── pom.properties
            ├── myproj_web.competitor-1.0-SNAPSHOT.jar
            ├── myproj_web.competitor-1.0-SNAPSHOT-sources.jar
            └── test-classes

1. all is a parent module containing the top pom.xml
2. biz is the module which contains the persistence parts(business logic)
3. web deals with the view.

1. http://localhost:8080/competitor/.dox?action=TemplateAction&event_submit_do_template=true&param=hello
competitor:app
>>>competitor: module name
>>>TemplateAction:TemplateAction.java class
>>>event_submit_do_Template<==>doTemplate() method in TemplateAction
>>>param:one parameters of in doTemplate


