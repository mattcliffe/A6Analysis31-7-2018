clear all;
clc


fnames = dir('*.CSV')

x=length(fnames);

figure(1)
clf()

for lmn = 1:x
    
    Data=importfile(fnames(lmn).name);
    
    save([fnames(lmn).name(1:8),'.mat'],'Data')
    PmrWindow = 6*60;
    Pmr = movmean(Data.PMr,[PmrWindow 0 ]);
    
    
    figure(1)
    plot(Data.DateTime,Pmr)
    hold on
    drawnow()
    
end



