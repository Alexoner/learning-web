#!/bin/sh

mvn archetype:generate \
    -DgroupId=com.howtodoinjava.ibatis.demo \
    -DartifactId=ibatisHelloWorld \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DinteractiveMode=false
