# Add your existing code to directory generated by the NLeSC Python template

1. Follow the [instructions to create a new package](https://github.com/NLeSC/python-template#how-to-use) with the Python template, while answering the questions like you would for the existing package.

2. Create a Git structure for the new directory: (replace the capitalized name by your own)
```shell
$ cd NEW_DIRECTORY
$ git init
$ git add --all
$ git commit -m "first commit"
$ git branch -M main
```

3. Import the existing repository from Github (Replace `<ORGANIZATION>` with your GitHub organization name , `REPOSITORY` with your GitHub repository name and `<BRANCH>` with your default branch for example `main` or `master`):
```shell
$ git remote add -f EXISTING_PACKAGE https://github.com/ORGANIZATION/EXISTING_PACKAGE
$ git merge EXISTING_PACKAGE/main --allow-unrelated-histories
```

4. The previous step will likely result in several merge conflicts. Solve the conflicts by editing the files and add the files to  Git:
```shell
$ EDITOR CONFLICT_FILES
$ git add --all
```
5. Push the new repository to Github:
```shell
$ git remote add origin https://github.com/ORGANIZATION/EXISTING_PACKAGE
$ git push
```