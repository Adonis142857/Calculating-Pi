#!/bin/bash

# 检查Python版本和pip
check_python() {
    if command -v python3 &>/dev/null; then
        version=$(python3 -c "import sys; print(sys.version_info.major, sys.version_info.minor)")
        if [[ $version < "3.7" ]]; then
            echo "Python版本过低，需要3.7及以上版本"
            install_python
        else
            echo "Python 3.7 及以上版本已安装"
        fi
    else
        echo "Python没有安装"
        install_python
    fi

    if command -v pip3 &>/dev/null; then
        echo "pip3已安装"
    else
        echo "pip3没有安装"
        install_pip
    fi

    $(python3 -c "import numpy" &> /dev/null)
    if [[ $? -ne 0 ]]; then
        echo "numpy库没有安装"
        install_numpy
    else
        echo "numpy库已安装"
    fi
}

# 安装Python
install_python() {
    if [[ $OS == "Debian" ]]; then
        sudo apt-get update
        sudo apt-get install python3.7 -y
    elif [[ $OS == "Red Hat" ]]; then
        sudo yum update -y
        sudo yum install python3.7 -y
    fi
}

# 安装pip
install_pip() {
    if [[ $OS == "Debian" ]]; then
        sudo apt-get update
        sudo apt-get install python3-pip -y
    elif [[ $OS == "Red Hat" ]]; then
        sudo yum update -y
        sudo yum install python3-pip -y
    fi
}

# 安装numpy
install_numpy() {
    pip3 install numpy
}

# 检查操作系统
if [[ "$(uname)" == "Linux" ]]; then
    if [[ -f /etc/debian_version ]]; then
        OS="Debian"
    elif [[ -f /etc/redhat-release ]]; then
        OS="Red Hat"
    else
        echo "无法识别的Linux版本"
        exit 1
    fi
else
    echo "非Linux系统"
    exit 1
fi

check_python

# 运行Python脚本
for script in pell_formula.py monte_carlo.py monte_carlo_variation_line_to_circle.py monte_carlo_variation_point_to_square.py taylor_series.py gauss_legendre.py poisson_formula.py; do
    nohup python3 "$script" > /dev/null 2>&1 &
done
