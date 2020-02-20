# class Filter
class Filter(self):
    
    def __init__(self):
        self.alpha_low_0 = [1, -1.979133761292768, 0.979521463540373]
        self.beta_low_0 = [0.000086384997973502, 0.000172769995947004, 0.000086384997973502]
        
        self.alpha_low_5 = [1, -1.80898117793047, 0.827224480562408]
        self.beta_low_5 = [0.095465967120306, -0.172688631608676, 0.095465967120306]
        
        self.alpha_high_1 = [1, -1.905384612118461, 0.910092542787947]
        self.beta_high_1 = [0.953986986993339, -1.907503180919730, 0.953986986993339]

    def low_0_filter(self, data):
        filtered_data = [0, 0]
        for i in range(2, len(data)): # from len to 2
            filtered_data = self.alpha_low_0 * (data[i] * self.beta_low_0[0] +
                                                data[i-1] * self.beta_low_0[1] +
                                                data[i-2] * self.beta_low_0[2] -
                                                filtered_data[i-1] * self.alpha_low_0[1] -
                                                filtered_data[i-2] * self.alpha_low_0[2])
        return filtered_data
            
    def low_5_filter(self, data):
        filtered_data = [0, 0]
        for i in range(2, len(data)):           
            filtered_data = self.alpha_low_5 * (data[i] * self.beta_low_5[0] +
                                                data[i-1] * self.beta_low_5[1] +
                                                data[i-2] * self.beta_low_5[2] -
                                                filtered_data[i-1] * self.alpha_low_5[1] -
                                                filtered_data[i-2] * self.alpha_low_5[2])
        return filtered_data
    
    def high_1_filter(self, data):
        filtered_data = [0, 0]
        for i in range(2, len(data)):  
            filtered_data = self.alpha_high_1 * (data[i] * self.beta_high_1[0] +
                                                data[i-1] * self.beta_high_1[1] +
                                                data[i-2] * self.beta_high_1[2] -
                                                filtered_data[i-1] * self.alpha_high_1[1] -
                                                filtered_data[i-2] * self.alpha_high_1[2])
        return filtered_data


# TODO: fix this parser
class Parser(self, data):
    
    def __init__(self, data):
        self.raw_data = data
        self.parsed_data = []

    def parse(self):
        self.parsed_data.append(data.split(';'))
        
  def parse
    @parsed_data = @data.to_s.split(';').map { |x| x.split('|') }
                   .map { |x| x.map { |x| x.split(',').map(&:to_f) } }

#     unless @parsed_data.map { |x| x.map(&:length).uniq }.uniq == [[3]]
#       raise 'Bad Input. Ensure data is properly formatted.'
#     end

#     if @parsed_data.first.count == 1
#       filtered_accl = @parsed_data.map(&:flatten).transpose.map do |total_accl|
#         grav = Filter.low_0_hz(total_accl)
#         user = total_accl.zip(grav).map { |a, b| a - b }
#         [user, grav]
#       end

#       @parsed_data = @parsed_data.length.times.map do |i|
#         user = filtered_accl.map(&:first).map { |elem| elem[i] }
#         grav = filtered_accl.map(&:last).map { |elem| elem[i] }
#         [user, grav]
#       end
#     end
#   end

# end

class Processor(self, data):
# Processor first calculte the dot product then pass it through two filters
    def __init__(self, data):
        self.dot_product_data = []
        for i in range(len(data())):
            self.dot_product_data.append(data[0][0] * data[1][0] + 
                                         data[0][1] * data[1][1] + data[0][2] * data[1][2])

    def filter(self):
        filter = Filter()
        filtered_data = filter.low_5_filter(self.dot_product_data)
        filtered_data = filter.high_1_filter(filtered_data)
        return filtered_data


class User(self, gender, height):
# use the data of an user to calculate a stride
    def __init__(self, gender, height):
        self.height = height
        self.gender = gender
        self.parameter = {'female multiplier': 0.413, 'female average': 0.413,
                     'male multiplier': 0.415, 'male average': 78.0}
        
        

    def calculate_stride(self):
        if gender.lower() == 'female':
            stride = self.height * self.parameter['female multiplier'] / 2
        elif gender.lower() == 'male':
            stride = self.height * self.parameter['male multiplier'] / 2

        return stride


# we ignore Trial class


class Analyzer(self, data, user):
    def __init__(self, data, user):
        self.THRESHOLE = 0.09
        self.data = data
        self.user = user


    def measure_steps(self):
        steps = 0
        count_steps = True
        
       for i in range(1, len(data)):
           if data[i] >= self.THRESHOLE && data[i-1] < self.THRESHOLE:
               if count_steps:
                   steps = steps + 1
                   count_steps = False
            
            if data[i] < 0 and data[i-1] >= 0:
                count_steps = True
        


#   def measure_delta
#     @delta = @steps - @trial.steps if @trial.steps
#   end

#   def measure_distance
#     @distance = @user.stride * @steps
#   end

#   def measure_time
#     @time = @data.count/@trial.rate if @trial.rate
#   end

# end

class Pipeline

  attr_reader :data, :user, :trial, :parser, :processor, :analyzer

  def self.run(data, user, trial)
    pipeline = Pipeline.new(data, user, trial)
    pipeline.feed
    pipeline
  end

  def initialize(data, user, trial)
    @data  = data
    @user  = user
    @trial = trial
  end

  def feed
    @parser    = Parser.run(@data)
    @processor = Processor.run(@parser.parsed_data)
    @analyzer  = Analyzer.run(@processor.filtered_data, @user, @trial)
  end

end

get '/uploads' do
  @error = "A #{params[:error]} error has occurred." if params[:error]
  @pipelines = Upload.all.inject([]) do |a, upload|
    a << Pipeline.run(File.read(upload.file_path), upload.user, upload.trial)
    a
  end

  erb :uploads
end

get '/upload/*' do |file_path|
  upload = Upload.find(file_path)
  @pipeline = Pipeline.run(File.read(file_path), upload.user, upload.trial)

  erb :upload
end

post '/create' do
  begin
    Upload.create(params[:data][:tempfile], params[:user], params[:trial])

    redirect '/uploads'
  rescue Exception => e
    redirect '/uploads?error=creation'
  end
end

