data = load('Ver_2_CS170_Fall_2021_LARGE_data__27.txt');
num_correct = 0;

for i = 1 : size(data,1)
    obj_2_class = data(i,2:end);
    label_object = data(i,1);
    nn_dist = inf;
    nn_loc = inf;
    for k = 1 : size(data,1)
        if k~= i
            distance = sqrt(sum((obj_2_class - data(k,2:end)).^2));
            if distance < nn_dist
                nn_dist = distance;
                nn_loc = k;
                nn_label = data(nn_loc,1);
            end
        end
    end
    if label_object == nn_label
        num_correct = num_correct + 1;
    end
    accuracy = num_correct / size(data,1);
    
end