FROM python:3.7

WORKDIR /app

# Update packages
RUN apt-get update -y

# Install ZSH
RUN apt-get install -y zsh

# Install required APT packages
ADD docker/apt.packages /tmp/apt.packages

RUN apt-get install -y $(awk '{print $1}' /tmp/apt.packages)

RUN rm -f /tmp/apt.packages

# Install Python requirements
ADD requirements.txt test-requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt -r /tmp/test-requirements.txt

RUN rm -f /tmp/requirements.txt /tmp/test-requirements.txt

# Create new user and use it
RUN useradd -ms /bin/zsh puma
RUN chsh -s /bin/zsh puma
USER puma

# Configure ZSH for user
RUN zsh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

# Infinite loop on startup
CMD exec /bin/zsh -c "trap : TERM INT; sleep infinity & wait"

