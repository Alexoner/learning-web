#!/bin/sh

mvn archetype:generate \
-DgroupId=com.alibaba.webx \
-DartifactId=webx-tutorial \
-Dversion=1.0-SNAPSHOT \
-Dpackage=com.alibaba.webx.tutorial1 \
-DarchetypeArtifactId=archetype-webx-quickstart \
-DarchetypeGroupId=com.alibaba.citrus.sample \
-DarchetypeVersion=1.8 \
-DinteractiveMode=false
