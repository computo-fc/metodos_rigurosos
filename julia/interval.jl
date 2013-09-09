import Base.show

abstract Inter

type Interval <: Inter
    lower
    upper
    
    Interval(lower, upper) = lower > upper ? error("out of order, lower needs to be <= upper!!!") : new(lower,upper)

    function Interval(lower)
        upper = lower
        new(lower, upper)
    end
end


type U

    intervals

    function U(intervals...)
       lista_intervalos = Inter[intervals[1]]
            for i in intervals
                g = x -> i == x

                if !any(map(g, lista_intervalos))
                
                    append!(lista_intervalos, [i])
                end
            end

        new([i for i in lista_intervalos])
    end
end



function show(io::IO, u::U)
    print(io,"Union of Intervals:\n")       
    for i = u.intervals
        println(io,"[$(i.lower), $(i.upper)]")
    end
end


function hull(x::Interval, y::Interval)
    Interval(min(x.lower, y.lower), max(x.upper, y.upper))
end


function (==)(x::Interval, y::Interval)

    if x.lower == y.lower && x.upper == y.upper
        return true
    else
        return false
    end
end


(+)(x::Inter, y::Inter) = Interval(x.lower + y.lower, x.upper + y.upper)

(+)(x::Interval, y::U) = U([x+i for i in y.intervals])

(+)(x::U, y::Interval) = (+)(y,x)

(+)(x::U, y::U) = U([i+j for i in x.intervals, j in y.intervals ])


(-)(x::Interval, y::Interval) = Interval(x.lower - y.upper, x.upper - y.lower)

(-)(x::Interval, y::U) = U([x-i for i in y.intervals])

(-)(x::U, y::Interval) = (-)(y,x)

(-)(x::U, y::U) = U([i-j for i in x.intervals, j in y.intervals ])



function (*)(x::Interval, y::Interval)
    
    a = x.lower
    b = x.upper
    c = y.lower
    d = y.upper

    vals = a*c, a*d, b*c, b*d

    Interval(min(vals), max(vals))
end

(*)(x::Interval, y::U) = U([x*i for i in y.intervals])

(*)(x::U, y::Interval) = (*)(y,x)

(*)(x::U, y::U) = U([i*j for i in x.intervals, j in y.intervals ])



        
function reciprocal(x::Interval)
    if x.lower <= 0 <= x.upper
        return U([Interval(-Inf, 1/x.lower), Interval(1/x.upper, Inf)])
    else
        return Interval(1.0/x.upper, 1.0/x.lower)
    end
end


function (/)(x::Interval, y::Interval)

    y = reciprocal(y)
    ans = x*y

        if isa(ans, U) && length(ans.intervals) == 1
            return ans.intervals[1]
        else
            return ans
        end
end

function show(io::IO, x::Interval)
    print(io, "[$(x.lower), $(x.upper)]")
end


function width(x::Interval)
    x.upper - x.lower
end

function middle(x::Interval)
    (x.upper + x.lower)/2.0
end

function radius(x::Interval)
    width(x)/2.0
end


function intersection(intervalos...)
    
    arreglo_intervalos = [i for i in intervalos]

    aux = arreglo_intervalos[1]
    
    for i = (2:length(intervalos))
        if aux.upper > intervalos[i].lower && aux.lower < intervalos[i].upper
        
            lo = max(aux.lower, intervalos[i].lower)
            hi = min(aux.upper, intervalos[i].upper)
            
            aux = Interval(lo, hi)
        else
            aux = None
        end        
    end
    return aux
end


function overlap(x::Interval, y::Interval)
    if intersection(x,y) != None
        return true
    else
        return false
    end
end
        


    

#function clean_union(u::U)
#    #Esta función simplifica la union de intervalos, juntando intervalos que se traslapan
##     
#    new_array = Interval[]
#    overlapping_array = Array[]
#     
##    
#     for i = 1:length(u.intervals)
#        overlaps = map(x -> overlap(x, u.intervals[i]), u.intervals)
#        append!(overlapping_array, overlaps)
#     end
#     
#     for i = 1:length(u.intervals)
#        for j = 1:length(u.intervals)
#            
#            if overlapping_array[i, j]
#                append(new_array)
        
     
function <(x::Interval, y::Interval)
    if x.upper < y.lower
        return true
    else
        return false
    end
end

function >(x::Interval, y::Interval)
    if x.lower > y. upper
        return true
    else
        return false
    end
end      



    
    
    
    
    
    
    
    
    
    
    
    
    




