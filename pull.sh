#!/bin/sh

git pull
cd santo/
if zip -rf ../santo.msk . ; then
	echo there was an archive, so I updated it
elif [ ! -f ../santo.msk ] ; then
	zip -r ../santo.msk .
	echo there was no archive, so I made one
else
	echo the archive is already up to date
fi


