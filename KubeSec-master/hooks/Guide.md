# Create dict

mkdir .git
mkdir hooks

# Run

In hooks directory:
cp pre-commit ../.git/hooks

Modify any file in the project.
git add .file
git commit -m 'any comment'
