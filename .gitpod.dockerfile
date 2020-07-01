FROM gitpod/workspace-full:latest

USER root
  
RUN mkdir /home/gitpod/.conda
# Install conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    conda create --prefix /workspace/conda/cthenv python=3.8 && \
    echo "conda activate /workspace/conda/cthenv" >> ~/.bashrc && \
    export PATH=/workspace/conda/cthenv/bin:$PATH && \
    source ~/.bashrc && \
    export SHELL=/bin/bash && \
    echo "conda install -y -c conda-forge jupyterlab" >> ~/.bashrc
    
#    echo "conda activate base" >> ~/.bashrc
    
RUN chown -R gitpod:gitpod /opt/conda \
    && chmod -R 777 /opt/conda \
    && chown -R gitpod:gitpod /home/gitpod/.conda \
    && chmod -R 777 /home/gitpod/.conda
 
