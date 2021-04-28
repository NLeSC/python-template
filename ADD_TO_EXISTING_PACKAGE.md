# Add to existing package

Here are instructions for using the Python template for an existing package

## Instructions

1. Apply the `cookiecutter` to the Python template to create a new package with the same name in temporary directory. Answer all questions like you would do for the existing package.
```shell
$ cd /tmp
$ cookiecutter https://github.com/NLeSC/python-template
package_name [my_python_package]: new_package
project_name [new_package]: new_package
...
```

2. Examine the new package to check if it contains files that are already present in you existing package. In our case we found four files: `README.md`, `LICENSE`, `.gitignore` and `CITATION.cff`

3. Move all non-duplicate files from the new package to the existing package, one-by-one. Immediately after moving a file, add it to the Git collection of the existing package
```shell
$ cd new_package
$ EXISTING_PACKAGE=/directory/existing_package
$ for FILE in * .[a-z]*
  do 
     if [ ! -f $EXISTING_PACKAGE/$FILE ]
     then
        mv -i $FILE $EXISTING_PACKAGE
        cd $EXISTING_PACKAGE
        git add $FILE
        cd -
     fi
  done
```

4. Decide what you want to do with the duplicate files. In our case, we decided to dicard the new files `LICENSE` and `CITATION.cff` in favor of the corresponding files in the existing packagae, and to concatenate the new files `README.md` and `.gitignore` to their corresponding existing ones.
```shell
$ ls -a
.   ..   CITATION.cff   LICENSE   README.md
$ cat README.md >> $EXISTING_PACKAGE/README.md
$ cat .gitignore >> $EXISTING_PACKAGE/.gitignore
$ rm -f CITATION.cff .gitignore LICENSE README.md
```

5. Edit the updated `README.md` to fix badges and remove unnecessary text

```shell
$ cd $EXISTING_PACKAGE
$ vim README.md
```

6. Commit the changes and push them to Github
```shell
$ git commit -m "included data from Python template" README.md .gitignore
$ git commit -m "imported from python template"
$ git push
```

