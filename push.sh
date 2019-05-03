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
  docker push gennyproject/${project}:latest
  docker push gennyproject/${project}:"${version}"
  docker push gennyproject/${project}:$(prop 'git.commit.id')
else
  echo "ERROR: git properties $file not found."
fi