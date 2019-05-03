#!/bin/bash

project=recommender

file="git.properties"

function prop {
    grep "${1}=" ${file}|cut -d'=' -f2
}

if [ -z "${1}" ]
then
   version="latest"
else
   version="${1}"
fi

if [ -f "$file" ]
then
  echo "$file found."

  echo "git.commit.id = " $(prop 'git.commit.id')
  docker build  -t gennyproject/${project}:${version} .
  docker tag gennyproject/${project}:${version} gennyproject/${project}:$(prop 'git.commit.id')
else
  echo "ERROR: git properties $file not found."
fi