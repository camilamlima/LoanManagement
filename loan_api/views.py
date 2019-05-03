from django.shortcuts import render, redirect


def test(request):
    return redirect('http://google.com.br')
