from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def cv(request):
    education = Education.objects.all()
    project = Project.objects.all()
    experience = Experience.objects.all()
    certificate = Certificate.objects.all()
    skill = Skill.objects.all()
    return render(request, 'cv.html', {'education':education , 'project':project , 'experience':experience, 'certificate':certificate , 'skill':skill })

@login_required
def edu_new(request):
    if request.method == "POST":
        form = EduForm(request.POST)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.save()
            return redirect('cv')
    else:
        form = EduForm()
    return render(request, 'add.html', {'form': form})

@login_required
def proj_new(request):
    if request.method == "POST":
        form = ProjForm(request.POST)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.save()
            return redirect('cv')
    else:
        form = ProjForm()
    return render(request, 'add.html', {'form': form})

@login_required
def exp_new(request):
    if request.method == "POST":
        form = ExpForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.save()
            return redirect('cv')
    else:
        form = ExpForm()
    return render(request, 'add.html', {'form': form})

@login_required
def cert_new(request):
    if request.method == "POST":
        form = CertForm(request.POST)
        if form.is_valid():
            cert = form.save(commit=False)
            cert.save()
            return redirect('cv')
    else:
        form = CertForm()
    return render(request, 'add.html', {'form': form})

@login_required
def ski_new(request):
    if request.method == "POST":
        form = SkiForm(request.POST)
        if form.is_valid():
            ski = form.save(commit=False)
            ski.save()
            return redirect('cv')
    else:
        form = SkiForm()
    return render(request, 'add.html', {'form': form})

@login_required
def edu_edit(request,pk):
    edu = get_object_or_404(Education, pk=pk)
    if request.method == "POST":
        form = EduForm(request.POST, instance=edu)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.save()
            return redirect('cv')
    else:
        form = EduForm(instance=edu)
    return render(request, 'add.html', {'form': form})

@login_required
def proj_edit(request,pk):
    proj = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjForm(request.POST, instance=proj)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.save()
            return redirect('cv')
    else:
        form = ProjForm(instance=proj)
    return render(request, 'add.html', {'form': form})

@login_required
def ski_edit(request,pk):
    ski = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        form = SkiForm(request.POST, instance=ski)
        if form.is_valid():
            ski = form.save(commit=False)
            ski.save()
            return redirect('cv')
    else:
        form = SkiForm(instance=ski)
    return render(request, 'add.html', {'form': form})

@login_required
def exp_edit(request,pk):
    exp = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = ExpForm(request.POST, instance=exp)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.save()
            return redirect('cv')
    else:
        form = ExpForm(instance=exp)
    return render(request, 'add.html', {'form': form})

@login_required
def cert_edit(request,pk):
    cert = get_object_or_404(Certificate, pk=pk)
    if request.method == "POST":
        form = CertForm(request.POST, instance=cert)
        if form.is_valid():
            cert = form.save(commit=False)
            cert.save()
            return redirect('cv')
    else:
        form = CertForm(instance=cert)
    return render(request, 'add.html', {'form': form})


@login_required
def edu_remove(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    edu.delete()
    return redirect('cv')

@login_required
def proj_remove(request, pk):
    proj = get_object_or_404(Project, pk=pk)
    proj.delete()
    return redirect('cv')

@login_required
def exp_remove(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    exp.delete()
    return redirect('cv')

@login_required
def cert_remove(request, pk):
    cert = get_object_or_404(Certificate, pk=pk)
    cert.delete()
    return redirect('cv')


@login_required
def ski_remove(request, pk):
    ski = get_object_or_404(Skill, pk=pk)
    ski.delete()
    return redirect('cv')
